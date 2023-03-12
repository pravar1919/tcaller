
// function getPostList() {
//     fetch('/contacts/')
//         .then(res=>res.json())
//         .then(data => {
//             renderContacts(data);
//         })
//         .catch(err => {
//         console.log(err)
//     })
// }

// function renderContacts(data) {
//     return data.map(contact => {
//         renderContact(contact);
//     })
// }

// function createNode(element) {
//     return document.createElement(element);
// }


// function append(parent, el) {
//     return parent.appendChild(el)
// }

// function renderContact(contact) {
//     const root = document.getElementById('root');
//     const div = createNode('div');
//     const name = createNode('h2');
//     const number = createNode('h2');
//     name.innerText = contact.name;
//     number.innerText = contact.contact_number
//     append(div, name);
//     append(div, number);

//     append(root, div);

    
// }

// getPostList()