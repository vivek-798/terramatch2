// File: properties.js
// This script handles the dynamic loading and filtering of property listings,
// and now includes functionality for requesting a site visit.

const API_URL = 'http://127.0.0.1:5000';

// DOM elements
const propertyListingsContainer = document.getElementById('property-listings');
const searchInput = document.getElementById('search-input');
const applyFiltersBtn = document.getElementById('apply-filters-btn');

// --- Functions to handle API calls and UI updates ---

/**
 * Fetches properties from the backend based on search and filter criteria.
 * @param {string} searchQuery The keyword to search for (district, mandal, description).
 * @param {string} landType The type of land to filter by.
 * @param {string} priceRange The price range to filter by (e.g., '100000-500000').
 */
async function fetchProperties(searchQuery = '', landType = '', priceRange = '') {
    // Show a loading message
    propertyListingsContainer.innerHTML = '<p class="loading-message">Loading properties...</p>';
    
    let url = `${API_URL}/properties/search?q=${searchQuery}&type=${landType}&price_range=${priceRange}`;

    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Server responded with status: ${response.status}`);
        }
        const properties = await response.json();
        renderProperties(properties);
    } catch (error) {
        console.error('Error fetching properties:', error);
        propertyListingsContainer.innerHTML = `<p class="loading-message">Error fetching properties: ${error.message}. Please check if the server is running.</p>`;
    }
}

/**
 * Renders a list of property objects into the HTML.
 * @param {Array} properties An array of property objects.
 */
function renderProperties(properties) {
    if (properties.length === 0) {
        propertyListingsContainer.innerHTML = '<p class="loading-message">No properties found matching your criteria.</p>';
        return;
    }

    propertyListingsContainer.innerHTML = ''; // Clear previous content

    properties.forEach(property => {
        const propertyCard = document.createElement('div');
        propertyCard.className = 'property-card';
        
        // Example of a placeholder image
        const placeholderImage = `https://placehold.co/400x200/cccccc/333333?text=${property.district}`;

        propertyCard.innerHTML = `
            <img src="${placeholderImage}" alt="Image of ${property.district}">
            <div class="property-card-content">
                <h3>${property.district}, ${property.mandal}</h3>
                <p class="location">${property.type_of_land} Land</p>
                <p class="price">₹${property.price.toLocaleString('en-IN')}</p>
                <div class="details">
                    <p>Size: ${property.size_acres} Acres</p>
                    <p>${property.description}</p>
                </div>
                <button class="site-visit-btn" data-property-id="${property.id}">Request Site Visit</button>
            </div>
        `;
        propertyListingsContainer.appendChild(propertyCard);
    });

    // Add event listeners to the newly created buttons
    document.querySelectorAll('.site-visit-btn').forEach(button => {
        button.addEventListener('click', handleSiteVisitRequest);
    });
}

/**
 * Handles the click event for the "Request Site Visit" button.
 * @param {Event} event The click event object.
 */
async function handleSiteVisitRequest(event) {
    const propertyId = event.target.dataset.propertyId;
    event.target.disabled = true;
    event.target.textContent = 'Requesting...';

    const url = `${API_URL}/request-site-visit`;
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ property_id: propertyId })
        });
        const result = await response.json();
        
        if (response.ok) {
            event.target.textContent = 'Request Sent!';
            event.target.style.backgroundColor = '#4CAF50';
        } else {
            // Handle error response from server
            event.target.textContent = result.message || 'Error';
            event.target.style.backgroundColor = '#f44336';
            console.error('Error:', result.error);
        }
    } catch (error) {
        event.target.textContent = 'Request Failed';
        event.target.style.backgroundColor = '#f44336';
        console.error('Fetch error:', error);
    }
}

// --- Event Listeners for user interaction ---

// Listen for clicks on the "Apply Filters" button
applyFiltersBtn.addEventListener('click', () => {
    const searchQuery = searchInput.value;
    // These dropdowns are not yet implemented in the HTML, so we will pass empty strings for now.
    const landType = ''; 
    const priceRange = ''; 
    fetchProperties(searchQuery, landType, priceRange);
});

// Listen for the "Enter" key in the search input
searchInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
        const searchQuery = searchInput.value;
        fetchProperties(searchQuery);
    }
});

// Initial call to fetch all properties when the page loads
document.addEventListener('DOMContentLoaded', () => {
    fetchProperties();
});
