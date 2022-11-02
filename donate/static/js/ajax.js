$(document).ready(function(){
    $.get("/donate/json", function(data) {
        for (i=0; i < data.length; i++){
            $(".wrapper-donate").append(`
            <div tabindex="-1" class="modal overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 w-full md:inset-0 h-modal md:h-screen">
                <div class="relative inline-block px-7 py-3 w-full max-w-lg h-screen md:h-auto">
                    <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
                        <div class="flex justify-between items-center p-5 rounded-t border-b dark:border-gray-600">
                            <h3 class="text-xl font-medium text-gray-900 dark:text-white">Verification</h3>
                            <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center dark:hover:bg-gray-600 dark:hover:text-white" data-modal-toggle="medium-modal">
                                <svg aria-hidden="true" class="x-modal w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
                                <span class="sr-only">Close modal</span> 
                            </button>
                        </div>
                        <div class="tasks p-6 space-y-6">
                            <p class="message text-base leading-relaxed text-gray-500 dark:text-gray-400">
                                Thank you! You have donated ${data[i].fields.nominal} and ${data[i].fields.jumlahPohon}x ${data[i].fields.namaPohon}.
                            </p>
                        </div>
                        <div class="flex items-center p-6 space-x-2 rounded-b border-t border-gray-200 dark:border-gray-600">
                            <button data-modal-toggle="medium-modal" type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">I accept</button>
                            <button data-modal-toggle="medium-modal" type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800 acc-button">I accept</button>
                            <button data-modal-toggle="medium-modal" type="button" class="text-gray-500 bg-white hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-gray-200 rounded-lg border border-gray-200 text-sm font-medium px-5 py-2.5 hover:text-gray-900 focus:z-10 dark:bg-gray-700 dark:text-gray-300 dark:border-gray-500 dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-gray-600 close-modal">Decline</button>
                        </div>
                    </div>
                </div>
            </div>
            `)
            const modal = document.querySelector('.modal');
            const acc = document.querySelector('.acc-button');
            const close = document.querySelector('.close-modal');
            const xModal = document.querySelector('.x-modal');
            close.addEventListener('click', function() {
                modal.classList.add('hidden')
            });
            xModal.addEventListener('click', function() {
                modal.classList.add('hidden')
            });
            acc.addEventListener('click', function() {
                location.href='/campaign'
            });
        }
    });

    $("#showModal").click(function(){
        const nominal = document.forms["donateForm"]["nominal"].value
        const namaPohon = document.forms["donateForm"]["namaPohon"].value
        const jumlahPohon = document.forms["donateForm"]["jumlahPohon"].value
        const pesan = document.forms["donateForm"]["pesan"].value
        const data = {nominal:nominal,namaPohon:namaPohon,jumlahPohon:jumlahPohon,pesan:pesan,csrfmiddlewaretoken:'{{ csrf_token }}'}
        $.ajax({url:"/donate/donate_ajax/",data:data,method:"POST"}).done(function (resp) {
            alert(data.nominal)
            $(".wrapper-donate").append(`
            <div tabindex="-1" class="modal overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 w-full md:inset-0 h-modal md:h-screen">
                <div class="relative inline-block px-7 py-3 w-full max-w-lg h-screen md:h-auto">
                    <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
                        <div class="flex justify-between items-center p-5 rounded-t border-b dark:border-gray-600">
                            <h3 class="text-xl font-medium text-gray-900 dark:text-white">Verification</h3>
                            <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center dark:hover:bg-gray-600 dark:hover:text-white" data-modal-toggle="medium-modal">
                                <svg aria-hidden="true" class="x-modal w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
                                <span class="sr-only">Close modal</span> 
                            </button>
                        </div>
                        <div class="tasks p-6 space-y-6">
                            <p class="message text-base leading-relaxed text-gray-500 dark:text-gray-400">
                                Thank you! You have donated ${resp.fields.nominal} and ${resp.fields.jumlahPohon}x ${resp.fields.namaPohon}.
                            </p>
                        </div>
                        <div class="flex items-center p-6 space-x-2 rounded-b border-t border-gray-200 dark:border-gray-600">
                            <button data-modal-toggle="medium-modal" type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">I accept</button>
                            <button data-modal-toggle="medium-modal" type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800 acc-button">I accept</button>
                            <button data-modal-toggle="medium-modal" type="button" class="text-gray-500 bg-white hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-gray-200 rounded-lg border border-gray-200 text-sm font-medium px-5 py-2.5 hover:text-gray-900 focus:z-10 dark:bg-gray-700 dark:text-gray-300 dark:border-gray-500 dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-gray-600 close-modal">Decline</button>
                        </div>
                    </div>
                </div>
            </div>
            `)
            const modal = document.querySelector('.modal');
            const acc = document.querySelector('.acc-button');
            const close = document.querySelector('.close-modal');
            const xModal = document.querySelector('.x-modal');
            close.addEventListener('click', function() {
                modal.classList.add('hidden')
            });
            xModal.addEventListener('click', function() {
                modal.classList.add('hidden')
            });
            acc.addEventListener('click', function() {
                location.href='/campaign'
            });
        })
    })
});