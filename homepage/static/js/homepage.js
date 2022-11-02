$(document).ready(() => {
    $('#submit-btn').click(function(e) {
      e.preventDefault()
      let form = $('#question-form')
      $.ajax({
          type: 'POST',
          url: 'submit-question/',
          data: form.serialize(),
          success: (response) => {
            form.val();
            console.log(response);
            $('textarea[name=question]').val('');
            confirm("Question submitted");
          },
      })
      add_last_question(); 
    })
  })

function add_last_question(){
  $.get(
    '/get_last_question/',
    (res) => {
      console.log("bisa kok");
      $('#last-submit-question').empty();
      $('#last-submit-question').append(
        `
        ${res}
        `
      );
    }
  )
}
const getButton =  document.getElementById('get-count-btn');

function gege(){
  $.get(
    '/get-campaign-sum/',
    (res) => {
      console.log(res);
      $('#campaign-count').empty();
      $('#count-detail').empty();
      $('#campaign-count').append(
        `
        ${res}
        `
      )
      $('#count-detail').append(
        `
        campaigns has already been started in Ecoist

        `
      )
    }
    
  )
}

$(`#get-count-btn`).attr('onclick', `gege()`);
 