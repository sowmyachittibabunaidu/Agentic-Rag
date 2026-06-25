const API="http://127.0.0.1:8000";

async function ingestURL(){

    const url=document.getElementById("url").value;

    const response=await fetch(API+"/ingest",{

        method:"POST",

        headers:{

            "Content-Type":"application/json"

        },

        body:JSON.stringify({

            url:url

        })

    });

    const data=await response.json();

    alert(data.message);

}

async function askQuestion(){

    const query=document.getElementById("question").value;

    const response=await fetch(API+"/chat",{

        method:"POST",

        headers:{

            "Content-Type":"application/json"

        },

        body:JSON.stringify({

            query:query

        })

    });

    const data=await response.json();

    document.getElementById("answer").innerHTML=data.answer;

}
