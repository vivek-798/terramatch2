// data.js (or placed directly in your <script> tag)
const telanganaDistrictsData = [
    {
        name: "Adilabad",
        mandals: ["Adilabad (U)", "Adilabad (R)", "Bela", "Boath", "Gudihatnoor", "Indravelli", "Jainath", "Narnoor"]
    },
    {
        name: "Bhadradri Kothagudem",
        mandals: ["Allapalli", "Annapureddypalli", "Aswaraopeta", "Bhadrachalam", "Burgampahad", "Chandrugonda", "Chunchupalle", "Dammapeta", "Dummugudem", "Gundala", "Julurpadu", "Karakagudem", "Kothagudem", "Laxmidevipalli", "Manuguru", "Mulakalapalli", "Palwancha", "Pinapaka", "Sujathanagar", "Tekulapalli", "Yellandu"]
    },
    {
        name: "Hyderabad",
        mandals: ["Amberpet", "Ameerpet", "Asifnagar", "Bahadurpura", "Bandlaguda", "Charminar", "Golkonda", "Himayatnagar", "Khairtabad", "Marredpally", "Musheerabad", "Nampally", "Saidabad", "Shaikpet", "Secunderabad", "Trimulgherry"]
    },
    {
        name: "Jagtial",
        mandals: ["Bheerpur", "Buggaram", "Dharmapuri", "Gollapalli", "Ibrahimpatnam", "Jagtial", "Jagtial (Rural)", "Kathlapur", "Kodimial", "Korutla", "Mallapur", "Mallial", "Metpalli", "Pegadapalli", "Raikal", "Sarangapur", "Velgatur"]
    },
    {
        name: "Jangaon",
        mandals: ["Bachannapeta", "Devaruppala", "Ghanpur (Stn)", "Jangaon", "Lingalaghanpur", "Narmetta", "Palakurthi", "Raghunathapalle", "Tharigoppula", "Zaffergadh"]
    },
    {
        name: "Jayashankar Bhupalpally",
        mandals: ["Bhimadevarpalle", "Bhupalpally", "Chityal", "Eturunagaram", "Ghanpur", "Guduru", "Kannaigudem", "Kataram", "Mahadevpur", "Mahamutharam", "Malharrao", "Mangapet", "Mogullapalle", "Mulugu", "Palimela", "Regonda", "Tadvai", "Tekumatla", "Vajedu", "Venkatapur"]
    },
    {
        name: "Jogulamba Gadwal",
        mandals: ["Alampur", "Atmakur", "Gadwal", "Itikyal", "Kaloor", "Khairatao", "Maldakal", "Manopad", "Nadira", "Rajoli", "Undavelly", "Wadepalle"]
    },
    {
        name: "Kamareddy",
        mandals: ["Banswada", "Bhiknoor", "Birkoor", "Domakonda", "Gandhari", "Kamareddy", "Lingampet", "Marpally", "Naga Reddipet", "Rajampet", "Sadasivanagar", "Tadwai", "Yellareddy"]
    },
    {
        name: "Karimnagar",
        mandals: ["Bollapalli", "Choppadandi", "Gangadhara", "Ganneruvaram", "Huzurabad", "Jammikunta", "Karimnagar (Rural)", "Karimnagar (Urban)", "Koheda", "Manakondur", "Mutharam", "Ramadugu", "Shankarapatnam", "Thimmapur", "Veenavanka"]
    },
    {
        name: "Khammam",
        mandals: ["Bonakal", "Burgampad", "Chintakani", "Enkuru", "Kalluru", "Khammam (Rural)", "Khammam (Urban)", "Konijerla", "Madhira", "Mamidikuduru", "Mudigonda", "Nelakondapalli", "Palair", "Penuballi", "Sathupalli", "Singareni", "Thallada", "Vemsoor", "Wyra", "Yerrupalem"]
    },
    {
        name: "Kumuram Bheem Asifabad",
        mandals: ["Asifabad", "Bejjur", "Chintalamanepally", "Dahegaon", "Jainoor", "Kagaznagar", "Kerameri", "Kouthala", "Lingapur", "Nennel", "Penchikalpet", "Rebbena", "Sirpur (T)", "Sirpur (U)", "Tiryani", "Wankidi"]
    },
    {
        name: "Mahabubabad",
        mandals: ["Bayyaram", "Dantalapally", "Dornakal", "Gudur", "Kothagudem", "Kuravi", "Mahabubabad", "Maripeda", "Nellikudur", "Peddavangara", "Thorrur"]
    },
    {
        name: "Mahabubnagar",
        mandals: ["Addakal", "Bhoothpur", "Balanagar", "C.C. Kunta", "Devarkadra", "Gandeed", "Hanwada", "Jadcherla", "Kothakota", "Mahabubnagar", "Midjil", "Moosapet", "Nawabpet", "Palamoor", "Rajapur"]
    },
    {
        name: "Mancherial",
        mandals: ["Bellampally", "Bheemini", "Chennur", "Dandepally", "Hajipur", "Jaipur", "Jannaram", "Kasipet", "Kotapally", "Luxettipet", "Mancherial", "Mandamarri", "Naspur", "Nennel", "Tandur", "Vempally"]
    },
    {
        name: "Medak",
        mandals: ["Alladurg", "Chegunta", "Kowdipalle", "Kulcharam", "Medak", "Narsapur", "Papannapet", "Ramayampet", "Shivampet", "Tekmal", "Tupran", "Yeldurthy"]
    },
    {
        name: "Medchal-Malkajgiri",
        mandals: ["Alwal", "Bachupally", "Balanagar", "Dundigal Gandimaisamma", "Ghatkesar", "Kapra", "Keesara", "Kukatpally", "Malkajgiri", "Medchal", "Medipally", "Quthbullapur", "Shamirpet", "Uppal"]
    },
    {
        name: "Mulugu",
        mandals: ["Eturnagaram", "Govindaraopet", "Kannaigudem", "Mangapet", "Mulugu", "Tadvai", "Vajedu", "Venkatapur"]
    },
    {
        name: "Nagarkurnool",
        mandals: ["Achampet", "Amrabad", "Balmoor", "Bijinapalle", "Kollapur", "Lingal", "Nagarkurnool", "Padra", "Pentlavelli", "Tadoor", "Telkapalle", "Thimmajipeta", "Uppunuthala"]
    },
    {
        name: "Nalgonda",
        mandals: ["Chandur", "Chinthapally", "Chityal", "Damaracherla", "Devarakonda", "Gundlapally", "Kattangur", "Miryalaguda", "Munugode", "Nalgonda", "Nampally", "Nidamanur", "Pedda Adiserlapally", "Thipparthy", "Tirumalagiri", "Valigonda", "Vemulapally", "Wadapally"]
    },
    {
        name: "Narayanpet",
        mandals: ["Amarchinta", "Atmakur", "Damaragidda", "Dhanwada", "Koilkonda", "Madgul", "Makthal", "Marikal", "Narayanpet", "Narva", "Utkoor"]
    },
    {
        name: "Nirmal",
        mandals: ["Basar", "Bhainsa", "Dilawarpur", "Kuntala", "Lokeshwaram", "Mudhole", "Narsapur (G)", "Nirmal", "Sarayapally", "Soan", "Tanur"]
    },
    {
        name: "Nizamabad",
        mandals: ["Armoor", "Bheemgal", "Bodh", "Donkeshwar", "Dichpally", "Gandhari", "Jakranpally", "Kamareddy", "Kotagiri", "Madnoor", "Morthad", "Navipet", "Nizamabad (Rural)", "Nizamabad (Urban)", "Perkit", "Ranjal", "Rudrur", "Sirikonda", "Varni", "Yedpally"]
    },
    {
        name: "Peddapalli",
        mandals: ["Basanthnagar", "Dharmaram", "Jaffargadh", "Kamanpur", "Manthani", "Mutharam", "Palakurthi", "Peddapalli", "Ramagundam", "Sultanabad"]
    },
    {
        name: "Rajanna Sircilla",
        mandals: ["Boinpally", "Chandurthi", "Gambhiraopet", "Kondapur", "Mustabad", "Rajanna Sircilla", "Thimmapur", "Vemulawada", "Yellareddypet"]
    },
    {
        name: "Ranga Reddy",
        mandals: ["Abdullapurmet", "Chevella", "Doma", "Farooqnagar", "Gandeed", "Ibrahimpatnam", "Kadthal", "Keshampet", "Kothur", "Maheswaram", "Moinabad", "Nagarkurnool", "Nandigama", "Pahadishareef", "Rajendranagar", "Serilingampally", "Shadnagar", "Shamshabad", "Shankarpally", "Thandur", "Vikarabad", "Yacharam"]
    },
    {
        name: "Sangareddy",
        mandals: ["Ameenpur", "Andole", "Gummadidala", "Hathnoora", "Jharasangam", "Jinnaram", "Kalher", "Kandi", "Kohir", "Kondapur", "Manoor", "Munipally", "Nagilgidda", "Narayankhed", "Nyalkal", "Patancheru", "Pulkal", "Raikode", "Ramchandrapuram", "Sadasivpet", "Sangareddy", "Sirgapoor", "Vatpally", "Zaheerabad"]
    },
    {
        name: "Siddipet",
        mandals: ["Akkannapet", "Bejjanki", "Cheriyal", "Chinnakodur", "Doultabad", "Dubbak", "Gajwel", "Husnabad", "Jagadevpur", "Kondapak", "Komuravelli", "Maddur", "Markook", "Mirdoddi", "Mulug", "Nangnoor", "Raipole", "Siddipet (Rural)", "Siddipet (Urban)", "Thoguta", "Wargal"]
    },
    {
        name: "Suryapet",
        mandals: ["Athmakur (S)", "Chilkur", "Chivvemla", "Garidepally", "Jajireddygudem", "Kodad", "Maddirala", "Mattampally", "Mothey", "Munagala", "Nadigudem", "Nagaram", "Neredcherla", "Nuthankal", "Pelluru", "Penpahad", "Suryapet", "Thirumalagiri", "Thungathurthy"]
    },
    {
        name: "Vikarabad",
        mandals: ["Basheerabad", "Bommaraspet", "Dharoor", "Doulthabad", "Kottapally", "Marpally", "Mogudampally", "Nawabpet", "Parigi", "Pudur", "Regode", "Tandur", "Vikarabad"]
    },
    {
        name: "Wanaparthy",
        mandals: ["Atmakur", "Chittapur", "Ghanpur", "Kothakota", "Pangala", "Pebbair", "Peddamandadi", "Revally", "Srirangapur", "Veepanagandla", "Wanaparthy"]
    },
    {
        name: "Warangal", // Formerly Warangal Urban & Rural, now split. Using a combined list for simplicity.
        mandals: ["Atmakur", "Damera", "Geesugonda", "Hanamkonda", "Kama-lapur", "Kazipet", "Khanapur", "Khila Warangal", "Madikonda", "Mogulapally", "Mulugu", "Nadikuda", "Narsampet", "Nekkonda", "Parkal", "Parvathagiri", "Rayaparthy", "Sangem", "Shayampet", "Wardhannapet", "Warangal", "Velair"]
    },
    {
        name: "Yadadri Bhuvanagiri",
        mandals: ["Addaguduru", "Alair", "Atmakur (M)", "Bhuvanagiri", "Bommalaremaram", "Choutuppal", "Gundala", "Motakondur", "Mothkur", " " , "Pochampally", "Ramannapet", "Thurkapally", "Valigonda", "Yadagirigutta"]
    }
];
document.addEventListener('DOMContentLoaded', () => {
    const districtsData = telanganaDistrictsData; // Use the data from data.js
    const districtsGrid = document.querySelector('.districts-grid');
    const showMoreBtn = document.getElementById('showMoreDistrictsBtn');
    const initialDistrictsToShow = 10;

    // Function to render district buttons
    function renderDistricts(data, limit = data.length) {
        districtsGrid.innerHTML = ''; // Clear existing content
        data.forEach((district, index) => {
            const districtWrapper = document.createElement('div');
            districtWrapper.classList.add('district-button-wrapper');
            if (index >= limit) {
                districtWrapper.classList.add('hidden'); // Hide beyond the limit
            }

            const button = document.createElement('button');
            button.classList.add('district-button');
            button.innerHTML = `
                <span>${district.name}</span>
                <span class="dropdown-arrow">&#9660;</span> `;
            button.setAttribute('data-district-name', district.name); // Store district name for lookup

            const mandalsDropdown = document.createElement('div');
            mandalsDropdown.classList.add('mandals-dropdown');
            
            district.mandals.forEach(mandal => {
                const mandalLink = document.createElement('a');
                mandalLink.href = `#${mandal.toLowerCase().replace(/\s+/g, '-')}`; // Example link
                mandalLink.textContent = mandal;
                mandalsDropdown.appendChild(mandalLink);
            });

            districtWrapper.appendChild(button);
            districtWrapper.appendChild(mandalsDropdown);
            districtsGrid.appendChild(districtWrapper);
        });

        // Set initial button text based on limit
        if (limit === initialDistrictsToShow && data.length > initialDistrictsToShow) {
            showMoreBtn.textContent = 'Show All Districts';
            showMoreBtn.style.display = 'block';
        } else if (limit === data.length && data.length > initialDistrictsToShow) {
            showMoreBtn.textContent = 'View Less';
            showMoreBtn.style.display = 'block';
        } else {
            showMoreBtn.style.display = 'none'; // Hide if all are shown and no more to hide, or if less than initialToShow
        }
    }

    // Initial render: show only the first 10 districts
    renderDistricts(districtsData, initialDistrictsToShow);

    // Event listener for "Show More/View Less" button
    showMoreBtn.addEventListener('click', () => {
        const currentlyHidden = districtsGrid.querySelectorAll('.district-button-wrapper.hidden').length > 0;

        if (currentlyHidden) {
            // Show all districts
            renderDistricts(districtsData, districtsData.length);
        } else {
            // Show only initial districts
            renderDistricts(districtsData, initialDistrictsToShow);
        }
    });

    // Event listener for district buttons (to toggle mandals dropdown)
    districtsGrid.addEventListener('click', (event) => {
        const clickedButton = event.target.closest('.district-button');
        if (clickedButton) {
            const currentWrapper = clickedButton.closest('.district-button-wrapper');
            const mandalsDropdown = currentWrapper.querySelector('.mandals-dropdown');

            // Close other open dropdowns
            document.querySelectorAll('.mandals-dropdown.show').forEach(dropdown => {
                if (dropdown !== mandalsDropdown) {
                    dropdown.classList.remove('show');
                    dropdown.previousElementSibling.classList.remove('active'); // Deactivate button
                }
            });

            // Toggle current dropdown
            mandalsDropdown.classList.toggle('show');
            clickedButton.classList.toggle('active'); // Activate/deactivate button
        }
    });

    // Close dropdowns when clicking outside
    document.addEventListener('click', (event) => {
        if (!event.target.closest('.district-button-wrapper') && !event.target.closest('.mandals-dropdown')) {
            document.querySelectorAll('.mandals-dropdown.show').forEach(dropdown => {
                dropdown.classList.remove('show');
                dropdown.previousElementSibling.classList.remove('active'); // Deactivate button
            });
        }
    });
});