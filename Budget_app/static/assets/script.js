const add_type = document.querySelector(".add__type");
const add__description = document.querySelector(".add__description");
const add__value = document.querySelector(".add__value");
const add__btn = document.querySelector(".add__btn");
const delete_items = document.querySelectorAll('.item__delete--btn')

// /////////// csrf token /////////////////


function getToken(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  var csrftoken = getToken("csrftoken");

////////////////////////////

budget_info = {
    Type: "inc",
    description: "",
    value: "",
}

function get_budget_info(field) {
  field.addEventListener("input", (ev) => {
    budget_info[ev.target.getAttribute("data-label")] = ev.target.value;
  });
}

get_budget_info(add_type)
get_budget_info(add__description)
get_budget_info(add__value)

add__btn.addEventListener("click", (ev) => {

  var add_budget = "/add_budget/";
  
  fetch(add_budget, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify(budget_info),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      
    });
    
    location.reload()
    
  });
  

delete_items.forEach((cur) => {
  cur.addEventListener('click', (ev) => {

    let id = ev.target.parentElement.getAttribute("data-label")

    fetch(`/delete_item/${id}/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
      },
      body: JSON.stringify({}),
    })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      
    });
    
    location.reload()

  })
})