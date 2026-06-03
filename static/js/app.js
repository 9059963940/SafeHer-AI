function sendSOS() {

    alert(
        "🚨 SOS ALERT SENT TO EMERGENCY CONTACTS!"
    );
}


async function checkRisk() {

    let msg =
        document.getElementById("message").value;

    let response = await fetch("/predict", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            message: msg
        })

    });

    let data = await response.json();

    document.getElementById("result")
        .innerText = data.result;
}


function getLocation() {

    if (navigator.geolocation) {

        navigator.geolocation.getCurrentPosition(

            function (position) {

                document.getElementById("location")
                    .innerHTML =

                    "Latitude: " +
                    position.coords.latitude +

                    "<br>Longitude: " +
                    position.coords.longitude;

            },

            function () {

                alert("Location access denied.");

            }

        );
    }

}


async function findNearby() {

navigator.geolocation.getCurrentPosition(

async function(position){

try{

let lat = position.coords.latitude;
let lon = position.coords.longitude;

let response =
await fetch(`/nearby?lat=${lat}&lon=${lon}`);

let data = await response.json();

let list =
document.getElementById("places");

list.innerHTML = "";

if(data.success){

let heading1 =
document.createElement("h4");

heading1.innerText =
"🏥 Hospitals";

list.appendChild(heading1);

data.hospitals.forEach(place=>{

let li =
document.createElement("li");

li.innerText =
place.display_name;

list.appendChild(li);

});

let heading2 =
document.createElement("h4");

heading2.innerText =
"👮 Police Stations";

list.appendChild(heading2);

data.police.forEach(place=>{

let li =
document.createElement("li");

li.innerText =
place.display_name;

list.appendChild(li);

});

}
else{

list.innerHTML =
"<li>Error fetching places.</li>";

}

}
catch(error){

console.error(error);

}

});

}