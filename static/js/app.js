/*
=========================================================
SentiVision AI
Frontend JavaScript

Developed by:
Emad Ali
UID: 24BSC10027
=========================================================
*/


document.addEventListener(
    "DOMContentLoaded",
    function () {


        // =========================
        // Analyze Button Loading
        // =========================


        const form = document.querySelector("form");


        if (form) {


            form.addEventListener(
                "submit",
                function () {


                    const button =
                    form.querySelector(
                        "button[type='submit']"
                    );


                    if (button) {


                        button.innerHTML =
                        `
                        <span class="spinner-border spinner-border-sm"></span>
                        Analyzing...
                        `;


                        button.disabled = true;


                    }


                }
            );


        }




        // =========================
        // Text Area Character Counter
        // =========================


        const textarea =
        document.querySelector(
            "textarea"
        );


        if (textarea) {


            const counter =
            document.createElement(
                "small"
            );


            counter.className =
            "text-muted d-block mt-2";


            textarea.parentNode.appendChild(
                counter
            );



            function updateCounter(){


                counter.innerHTML =
                `
                Characters:
                ${textarea.value.length}
                `;


            }



            textarea.addEventListener(
                "input",
                updateCounter
            );


            updateCounter();


        }





        // =========================
        // Smooth Page Animation
        // =========================


        const cards =
        document.querySelectorAll(
            ".card"
        );


        cards.forEach(
            function(card,index){


                card.style.animationDelay =
                `${index * 0.08}s`;


            }
        );





        // =========================
        // Auto Hide Alerts
        // =========================


        const alerts =
        document.querySelectorAll(
            ".alert"
        );


        alerts.forEach(
            function(alert){


                setTimeout(
                    function(){


                        alert.style.transition =
                        "0.5s";


                        alert.style.opacity =
                        "0";


                    },
                    8000
                );


            }
        );




        // =========================
        // Dashboard Number Animation
        // =========================


        const numbers =
        document.querySelectorAll(
            ".display-5"
        );


        numbers.forEach(
            function(number){


                let value =
                parseInt(
                    number.innerText
                );


                if(!isNaN(value)){


                    let current = 0;


                    let interval =
                    setInterval(
                        function(){


                            current +=
                            Math.ceil(
                                value / 30
                            );


                            if(current >= value){

                                current=value;

                                clearInterval(
                                    interval
                                );

                            }


                            number.innerText =
                            current;


                        },
                        30
                    );


                }


            }
        );


    }
);