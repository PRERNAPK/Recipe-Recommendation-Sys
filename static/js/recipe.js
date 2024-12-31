// JavaScript to handle the click event on the recipe card
function showRecipeSteps(card) {
    // Get the overlay element and the steps inside the clicked card
    const overlay = document.createElement('div');
    overlay.classList.add('overlay');
    document.body.appendChild(overlay);
    
    // Show the recipe steps
    const steps = card.querySelector('.recipe-steps');
    steps.style.display = 'block';

    // Expand the card and center it
    card.classList.add('expanded-card');

    // Show the overlay (background dimming)
    overlay.style.display = 'block';

    // Close the expanded view when the overlay is clicked
    overlay.addEventListener('click', () => {
        overlay.style.display = 'none';  // Hide the overlay
        steps.style.display = 'none';    // Hide the steps
        card.classList.remove('expanded-card'); // Restore the card to its original size
        document.body.removeChild(overlay);  // Remove the overlay from the DOM
    });
}
