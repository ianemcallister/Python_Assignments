// script.js

// 1. Lightbox functionality for images
document.addEventListener("DOMContentLoaded", function () {
    const images = document.querySelectorAll("section img");
    const lightbox = document.createElement("div");
    lightbox.classList.add("lightbox");
    document.body.appendChild(lightbox);

    images.forEach((img) => {
        img.addEventListener("click", () => {
            const largeImage = document.createElement("img");
            largeImage.src = img.src;
            lightbox.innerHTML = "";
            lightbox.appendChild(largeImage);
            lightbox.classList.add("active");
        });
    });

    lightbox.addEventListener("click", () => {
        lightbox.classList.remove("active");
    });
});

// 2. Lazy loading for images
const imagesToLoad = document.querySelectorAll('section img');
const imgObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const img = entry.target;
            img.src = img.dataset.src; // Use data-src attribute for lazy loading
            imgObserver.unobserve(img);
        }
    });
});

imagesToLoad.forEach(img => {
    imgObserver.observe(img);
});

// 3. Scroll to the top button functionality
const scrollToTopBtn = document.createElement("button");
scrollToTopBtn.textContent = "Scroll to Top";
scrollToTopBtn.classList.add("scroll-to-top");
document.body.appendChild(scrollToTopBtn);

scrollToTopBtn.addEventListener("click", () => {
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
});

// Show/hide button based on scroll position
window.addEventListener("scroll", () => {
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        scrollToTopBtn.style.display = "block";
    } else {
        scrollToTopBtn.style.display = "none";
    }
});
