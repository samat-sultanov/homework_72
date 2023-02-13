function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

async function makeRequest(url, method = 'GET', headers, body) {
    let fetch_init = {method};
    if (method !== "GET") {
        fetch_init = {method, headers, body};
    }
    let response = await fetch(url, fetch_init);

    if (response.ok) {
        return await response.json();
    } else {
        let error = new Error(response.statusText);
        error.response = response;
        throw error;
    }
}

async function buttonClickGet(event) {

    let url = `${event.target.dataset['url']}`;
    try {
        let response = await makeRequest(url);
        let list = document.getElementById("myList");
        response.forEach((repo) => {
            Object.entries(repo).forEach(([key, value]) => {
                if (`${key}` === 'text') {
                    console.log(`${value}`);
                    let li = document.createElement("li");
                    li.innerText = `${value}`;
                    list.appendChild(li);
                }
            });
        });
    } catch (e) {
        console.log(await e.response.json());
    }
}

async function buttonClickPost(event) {
    let target = event.currentTarget;
    let text = document.getElementById('text');
    let author = document.getElementById('author');
    let email = document.getElementById('email');

    let url = `${event.target.dataset['add-url']}`;
    let headers = {'Content-Type': 'application/json', 'X-CSRFToken': csrftoken};
    let body = JSON.stringify({"text": text.value, "author": author.value, "email": email.value});
    try {
        let response = await makeRequest(url, "POST", headers, body);
    } catch (e) {
        console.log(await e.response.json());
    }
}

function load() {
    let buttonAddGet = document.getElementById('phrases_list');
    buttonAddGet.onclick = buttonClickGet;


    let buttonAddPhrase = document.getElementById('add_phrase');
    buttonAddPhrase.onclick = buttonClickPost;
}


window.addEventListener('load', load);