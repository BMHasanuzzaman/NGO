
            // Use JavaScript to dynamically generate HTML elements
            for (let i = 1; i <= 12; i++) {
                // Create a new div element
                var divElement = document.createElement('div');

                // Create an img element and set its source attribute
                var imgElement = document.createElement('img');
                imgElement.src = '/static/Images/' + i + '.jpg';

                // Append the img element to the div element
                divElement.appendChild(imgElement);

                // Append the div element to the container
                document.getElementById('imagegallery').appendChild(divElement);
            }