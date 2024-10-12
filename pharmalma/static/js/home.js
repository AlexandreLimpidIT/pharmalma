document.addEventListener("DOMContentLoaded", function() {
    const csrfToken = '{{ csrf_token }}';
    
    function redirectToCarte(event) {
        event.preventDefault(); 
        console.log("Le bouton a été cliqué."); 

        const ville = document.getElementById("ville").value;
        const medicament_name = document.getElementById("medicament").value;
        console.log("Ville :", ville, "Médicament :", medicament_name); 

        fetch('/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': csrfToken
            },
            body: `medicament=${encodeURIComponent(medicament_name)}`
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Erreur réseau : ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            console.log("Données reçues :", data);
            const pharmacies = data.pharmacies;

            if (pharmacies.length > 0) {
                const pointsArray = pharmacies.map(pharmacy => {
                    return { 
                        lat: pharmacy.lat, 
                        lng: pharmacy.lng, 
                        nom: pharmacy.nom, 
                        adresse: pharmacy.adresse, 
                        telephone: pharmacy.telephone 
                    }; 
                });

                const url = new URL('/carte', window.location.origin);
                url.searchParams.append('points', JSON.stringify(pointsArray));
                url.searchParams.append('ville', encodeURIComponent(ville));
                window.location.href = url.toString();
            } else {
                alert('Aucune pharmacie trouvée avec ce médicament.');
            }
        })
        .catch(error => {
            console.error('Erreur:', error);
            alert('Une erreur est survenue lors de la requête. Vérifiez la console pour plus de détails.');
        });
    }

    document.querySelector('form').addEventListener('submit', redirectToCarte);
});
