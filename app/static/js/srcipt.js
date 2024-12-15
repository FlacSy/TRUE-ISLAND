
async function getHighlights() {
    const highlightsContainer = document.getElementById('highlights-container');

    try {
        const response = await fetch(
            '/api/get_highlights',
            {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ limit: 4 }),
            }
        );

        const highlights = await response.json();

        for (const highlight of highlights) {
            const highlightElement = document.createElement('div');
            highlightElement.classList.add('highlight-item');
            try {
                highlightElement.innerHTML = `
                    <img src="${highlight.image_url}" alt="${highlight.title}">
                `;
                highlightsContainer.appendChild(highlightElement);
            } catch (error) {
                console.error(error);
            }
        }

    } catch (error) {
        console.error('Error fetching highlights:', error);
    }
}



async function generateAdvertisement() {
    const adContainer = document.getElementById('ad-container');

    try {
        const response = await fetch(
            '/api/get_advertisement',
            {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ limit: 2 }),
            }
        );

        const ads = await response.json();

        for (const ad of ads) {
            const adElement = document.createElement('div');
            adElement.classList.add('advertisement-item');
            try {
                adElement.innerHTML = `
                    <img src="${ad.image_url}" alt="${ad.title}">
                    <h2 class="ad-text">${ad.title}</h2>
                `;
                adContainer.appendChild(adElement);
            } catch (error) {
                console.error(error);
            }
        }

    } catch (error) {
        console.error('Error fetching advertisements:', error);
    }
}

async function selectLang() {
    document.getElementById("language-switch").addEventListener("click", async () => {
        const langElement = document.getElementById("select-lang");

        const currentLang = langElement.innerText;

        let newLang = "EN";

        if (currentLang === "ENG") {
            newLang = "PL";
        } else if (currentLang === "PL") {
            newLang = "ENG";
        } else {
            newLang = "ENG";
        }

        langElement.innerText = newLang;

    });
}


async function main() {
    await getHighlights();
    await generateAdvertisement();
    selectLang();
}

document.addEventListener('DOMContentLoaded', main);