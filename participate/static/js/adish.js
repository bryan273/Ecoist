

// Initial setup
function setup() {
    $.ajaxSetup({ // set up CSRF token for all HTTP requests
        headers: {"X-CSRFToken": $('[name=csrfmiddlewaretoken]').val()}
    });
    getTodolist();
    refreshForm();
}

async function getTodolist() {
    return fetch("{% url 'participate:show_json' %}")
    .then(response => response.json())
    .then(participants => {
      return participants;
    })
    .catch(error => {
      console.error("ERROR:", error);
    })
  }

async function refreshForm() {
  getTodolist().then(participants => {
    let todos = "";

      const card = `
      <div class="card">
              <p class="text-xl text-center">Thank you for participating, ${participants[participants.length-1].fields.nama_pendaftar}!</p>
              <hr/>
              <br>
              <p class="text-xl text-center">We will send further information regarding this campaign to ${participants[participants.length-1].fields.email_pendaftar} :) </p>
              <br>
      </div>
      `;

      todos += card;

    document.getElementById("tasks").innerHTML = todos;
  });
}

function addTodolist() {
    fetch("{% url 'participate:join_campaign' %}", {
          method: "POST",
          body: new FormData(document.querySelector('#userAccountSetupForm'))
      }).then(refreshForm)
    return false
  }

  document.getElementById("butts").onclick = addTodolist()
  refreshForm()

const navigateToFormStep = (stepNumber) => {
    /**
     * Hide all form steps.
     */
    document.querySelectorAll(".form-step").forEach((formStepElement) => {
        formStepElement.classList.add("d-none");
    });
    /**
     * Mark all form steps as unfinished.
     */
    document.querySelectorAll(".form-stepper-list").forEach((formStepHeader) => {
        formStepHeader.classList.add("form-stepper-unfinished");
        formStepHeader.classList.remove("form-stepper-active", "form-stepper-completed");
    });
    /**
     * Show the current form step (as passed to the function).
     */
    document.querySelector("#step-" + stepNumber).classList.remove("d-none");
    /**
     * Select the form step circle (progress bar).
     */
    const formStepCircle = document.querySelector('li[step="' + stepNumber + '"]');
    /**
     * Mark the current form step as active.
     */
    formStepCircle.classList.remove("form-stepper-unfinished", "form-stepper-completed");
    formStepCircle.classList.add("form-stepper-active");
    /**
     * Loop through each form step circles.
     * This loop will continue up to the current step number.
     * Example: If the current step is 3,
     * then the loop will perform operations for step 1 and 2.
     */
    for (let index = 0; index < stepNumber; index++) {
        /**
         * Select the form step circle (progress bar).
         */
        const formStepCircle = document.querySelector('li[step="' + index + '"]');
        /**
         * Check if the element exist. If yes, then proceed.
         */
        if (formStepCircle) {
            /**
             * Mark the form step as completed.
             */
            formStepCircle.classList.remove("form-stepper-unfinished", "form-stepper-active");
            formStepCircle.classList.add("form-stepper-completed");
        }
    }
};
/**
 * Select all form navigation buttons, and loop through them.
 */
document.querySelectorAll(".btn-navigate-form-step").forEach((formNavigationBtn) => {
    /**
     * Add a click event listener to the button.
     */
    formNavigationBtn.addEventListener("click", () => {
        /**
         * Get the value of the step.
         */
        const stepNumber = parseInt(formNavigationBtn.getAttribute("step_number"));
        /**
         * Call the function to navigate to the target form step.
         */
        navigateToFormStep(stepNumber);
    });
});
  
document.addEventListener("DOMContentLoaded", function(event) {
    document.getElementById("share").onclick = function() {
    var share_icons = document.querySelector("#share_icons");
    check_opacity = share_icons.classList.contains('opacity-0');
    if (check_opacity) {
    share_icons.classList.remove('opacity-0');
    share_icons.classList.add('opacity-1');
    } else {
    share_icons.classList.remove('opacity-1');
    share_icons.classList.add('opacity-0');
    }
    };
    
    });


