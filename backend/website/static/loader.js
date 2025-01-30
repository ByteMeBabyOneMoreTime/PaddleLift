document.addEventListener("DOMContentLoaded", function() {
    // Create the spinner container element
    const spinnerContainer = document.createElement("div");
    spinnerContainer.id = "loading-container";
    spinnerContainer.style.position = "fixed";
    spinnerContainer.style.zIndex = "9999";
    spinnerContainer.style.top = "0";
    spinnerContainer.style.left = "0";
    spinnerContainer.style.width = "100%";
    spinnerContainer.style.height = "100%";
    spinnerContainer.style.backgroundColor = "#111827"; // Dark background
    spinnerContainer.style.display = "flex"; // Flexbox for centering
    spinnerContainer.style.justifyContent = "center"; // Center horizontally
    spinnerContainer.style.alignItems = "center"; // Center vertically
    spinnerContainer.style.transition = "opacity 1s ease-out"; // Fade out effect

    // Create the new spinner element (as per the provided HTML)
    const spinner = document.createElement("div");
    spinner.classList.add("spinner");

    const spinner1 = document.createElement("div");
    spinner1.classList.add("spinner1");

    spinner.appendChild(spinner1);
    spinnerContainer.appendChild(spinner);
    document.body.appendChild(spinnerContainer);

    // Add the styles for the spinner
    const style = document.createElement('style');
    style.innerHTML = `
        .spinner {
            background-image: linear-gradient(rgb(186, 66, 255) 35%, rgb(0, 225, 255));
            width: 100px;
            height: 100px;
            animation: spinning82341 1.7s linear infinite, hue 1s ease-in-out infinite;
            text-align: center;
            border-radius: 50px;
            filter: blur(1px);
            box-shadow: 0px -5px 20px 0px rgb(186, 66, 255), 0px 5px 20px 0px rgb(0, 225, 255);
        }
        
        .spinner1 {
            background-color: rgb(36, 36, 36);
            width: 100px;
            height: 100px;
            border-radius: 50px;
            filter: blur(10px);
        }
        
        @keyframes spinning82341 {
            to {
                transform: rotate(360deg);
            }
        }
        
        @keyframes hue {
            0% {
                filter: hue-rotate(0deg);
            }
            100% {
                filter: hue-rotate(360deg);
            }
        }
    `;
    document.head.appendChild(style);

    // Hide the spinner and fade out the background after 2 seconds
    setTimeout(function() {
        spinnerContainer.style.opacity = "0"; // Fade out the background
    }, 1000);  // 1000 milliseconds = 1 second

    // Remove the spinner after the fade-out effect
    setTimeout(function() {
        spinnerContainer.style.display = "none"; // Hide the spinner container after fade
    }, 1000);  // Wait for 1.5 seconds after fade for smooth removal
});
