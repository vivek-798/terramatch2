// File: price-estimation.js

// API URL for the Flask backend
const API_URL = 'http://127.0.0.1:5000';

// DOM elements
const form = document.getElementById('estimation-form');
const districtInput = document.getElementById('district');
const mandalInput = document.getElementById('mandal');
const typeoflandSelect = document.getElementById('typeofland');
const sizeInput = document.getElementById('size');
const estimateButton = document.getElementById('estimate-button');
const outputDiv = document.querySelector('.estimation .output');

const modal = document.getElementById('message-modal');
const closeButton = document.getElementById('close-message');
const messageText = document.getElementById('message-text');

// Create datalists for district and mandal inputs
const districtDataList = document.createElement('datalist');
districtDataList.id = 'district-list';
districtInput.setAttribute('list', 'district-list');
document.body.appendChild(districtDataList);

const mandalDataList = document.createElement('datalist');
mandalDataList.id = 'mandal-list';
mandalInput.setAttribute('list', 'mandal-list');
document.body.appendChild(mandalDataList);

// Function to show the modal with a message
function showMessageModal(message, isError = false) {
    messageText.textContent = message;
    if (isError) {
        messageText.classList.add('error');
        messageText.classList.remove('success');
    } else {
        messageText.classList.add('success');
        messageText.classList.remove('error');
    }
    modal.style.display = 'block';
}

// Function to fetch districts from the backend
async function fetchDistricts() {
    try {
        const response = await fetch(`${API_URL}/districts`);
        if (!response.ok) {
            throw new Error(`Server responded with status: ${response.status}`);
        }
        const districts = await response.json();
        districtDataList.innerHTML = ''; // Clear existing options
        districts.forEach(district => {
            const option = document.createElement('option');
            option.value = district;
            districtDataList.appendChild(option);
        });
    } catch (error) {
        console.error('Error fetching districts:', error);
        showMessageModal(`Failed to load districts: ${error.message}. Is the server running?`, true);
    }
}

// Function to fetch mandals for a given district from the backend
async function fetchMandals(district) {
    mandalDataList.innerHTML = ''; // Clear existing options
    if (!district) {
        return;
    }

    try {
        const response = await fetch(`${API_URL}/mandals/${district}`);
        if (!response.ok) {
            throw new Error(`Server responded with status: ${response.status}`);
        }
        const mandals = await response.json();
        mandals.forEach(mandal => {
            const option = document.createElement('option');
            option.value = mandal;
            mandalDataList.appendChild(option);
        });
    } catch (error) {
        console.error('Error fetching mandals:', error);
        showMessageModal('Failed to load mandals. Please check the district name.', true);
    }
}

// Event listener for district input change
districtInput.addEventListener('input', (e) => {
    const selectedDistrict = e.target.value.toLowerCase();
    fetchMandals(selectedDistrict);
});

// Event listener for form submission
form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const district = districtInput.value.toLowerCase();
    const mandal = mandalInput.value.toLowerCase();
    const landType = typeoflandSelect.value;
    const size = parseFloat(sizeInput.value);

    // Simple validation
    if (!district || !mandal || !landType || isNaN(size) || size <= 0) {
        outputDiv.innerHTML = '<p class="error-message">Please fill out all fields with valid data.</p>';
        return;
    }

    // Show a loading message while waiting for the response
    outputDiv.innerHTML = '<p>Calculating price...</p>';

    try {
        const response = await fetch(`${API_URL}/price/${district}/${mandal}`);
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || `Server responded with status: ${response.status}`);
        }
        const data = await response.json();
        let pricePerAcre = data.pricePerAcre;

        // Adjust price based on land type
        let priceMultiplier = 1.0;
        switch(landType.toLowerCase()) {
            case 'residential':
                priceMultiplier = 1.5;
                break;
            case 'commercial':
                priceMultiplier = 2.0;
                break;
            case 'industrial':
                priceMultiplier = 1.8;
                break;
            case 'other':
                priceMultiplier = 1.2;
                break;
            case 'agricultural':
            default:
                priceMultiplier = 1.0; // Agricultural is the base price
                break;
        }

        const adjustedPrice = pricePerAcre * priceMultiplier * size;
        
        outputDiv.innerHTML = `
            <p>Estimated Land Price:</p>
            <p class="estimated-price">₹${adjustedPrice.toLocaleString('en-IN', {
                maximumFractionDigits: 2,
                style: 'currency',
                currency: 'INR'
            })}</p>
        `;
    } catch (error) {
        console.error('Error checking price:', error);
        outputDiv.innerHTML = `<p class="error-message">Error: ${error.message}</p>`;
    }
});

// Event listener to close the modal
closeButton.onclick = function() {
  modal.style.display = "none";
}

// Close modal if user clicks outside of it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

// Initial call to populate the district datalist when the page loads
document.addEventListener('DOMContentLoaded', fetchDistricts);
