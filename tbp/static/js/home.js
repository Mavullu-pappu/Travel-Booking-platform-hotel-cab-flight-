 
        const tabs = document.querySelectorAll(".tab");
        const form = document.querySelector(".search-form");
        const source = document.getElementById("source");
        const destination = document.getElementById("destination");
        const date = document.getElementById("travel-date");

        tabs.forEach(tab => {
            tab.addEventListener("click", () => {
                tabs.forEach(t => t.classList.remove("active"));
                tab.classList.add("active");

                const type = tab.dataset.type;

                if (type === "flight") {
                    form.action = "/flights/";
                    source.placeholder = "Departure city";
                    destination.placeholder = "Destination city";
                    destination.parentElement.style.display = "flex";
                    date.previousElementSibling.textContent = "Travel Date";
                } else if (type === "hotel") {
                    form.action = "/hotels/";
                    source.placeholder = "Hotel location";
                    destination.parentElement.style.display = "none";
                    date.previousElementSibling.textContent = "Check-in Date";
                } else {
                    form.action = "/cabs/";
                    source.placeholder = "Pickup location";
                    destination.placeholder = "Drop location";
                    destination.parentElement.style.display = "flex";
                    date.previousElementSibling.textContent = "Pickup Date";
                }

                destination.required = type !== "hotel";
            });
        });
