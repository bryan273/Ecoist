// $(document).ready(function(){
    $.get("/donate/json", function(data) {
        for (i=0; i < data.length; i++){
            $(".wrapper-donate").append(`
            <div tabindex="-1" class="modal overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 w-full md:inset-0 h-modal md:h-screen">
                <div class="relative inline-block px-7 py-3 w-full max-w-lg h-screen md:h-auto">
                    <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
                        <div class="flex justify-center items-center p-5 rounded-t border-b dark:border-gray-600">
                            <h3 class="text-xl font-medium text-gray-900 dark:text-white">Success!</h3>
                        </div>
                        <div class="tasks p-6 space-y-6">
                            <p class="message text-base leading-relaxed text-gray-500 dark:text-gray-400">
                                Thank you! You have donated IDR ${data[i].fields.nominal} and ${data[i].fields.jumlahPohon}x ${data[i].fields.namaPohon}.
                            </p>
                        </div>
                        <div class="flex justify-center p-6 space-x-2 rounded-b border-t border-gray-200 dark:border-gray-600">
                            <button data-modal-toggle="medium-modal" type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800 acc-button">OK</button>
                            <button data-modal-toggle="medium-modal" type="button" class="text-gray-500 bg-white hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-gray-200 rounded-lg border border-gray-200 text-sm font-medium px-5 py-2.5 hover:text-gray-900 focus:z-10 dark:bg-gray-700 dark:text-gray-300 dark:border-gray-500 dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-gray-600 close-modal">Donate Again</button>
                        </div>
                    </div>
                </div>
            </div>
            `)
            $(".close-modal").click(function(){
                $(".modal").addClass("hidden")
            })
            $(".acc-button").click(function(){
                location.href='/campaign'
            })
        }
    });
    
    $("#showModal").click(function(){
        $(".modal").removeClass("hidden")
    })

    $("#showModal").click(function(){
        const nominal = document.forms["donateForm"]["nominal"].value
        const namaPohon = document.forms["donateForm"]["namaPohon"].value
        const jumlahPohon = document.forms["donateForm"]["jumlahPohon"].value
        const pesan = document.forms["donateForm"]["pesan"].value
        const data = {nominal:nominal,namaPohon:namaPohon,jumlahPohon:jumlahPohon,pesan:pesan,csrfmiddlewaretoken:'{{ csrf_token }}'}
        $.ajax({url:"/donate/donate_ajax/",data:data,method:"POST"}).done(function (resp) {
            $(".wrapper-donate").append(`
            <div tabindex="-1" class="modal overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 w-full md:inset-0 h-modal md:h-screen">
                <div class="relative inline-block px-7 py-3 w-full max-w-lg h-screen md:h-auto">
                    <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
                        <div class="flex justify-center items-center p-5 rounded-t border-b dark:border-gray-600">
                            <h3 class="text-xl font-medium text-gray-900 dark:text-white">Success!</h3>
                        </div>
                        <div class="tasks p-6 space-y-6">
                            <p class="message text-base leading-relaxed text-gray-500 dark:text-gray-400">
                                Thank you! You have donated IDR ${resp.fields.nominal} and ${resp.fields.jumlahPohon}x ${resp.fields.namaPohon}.
                            </p>
                        </div>
                        <div class="flex justify-center p-6 space-x-2 rounded-b border-t border-gray-200 dark:border-gray-600">
                            <button data-modal-toggle="medium-modal" type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800 acc-button">OK</button>
                            <button data-modal-toggle="medium-modal" type="button" class="text-gray-500 bg-white hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-gray-200 rounded-lg border border-gray-200 text-sm font-medium px-5 py-2.5 hover:text-gray-900 focus:z-10 dark:bg-gray-700 dark:text-gray-300 dark:border-gray-500 dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-gray-600 close-modal">Donate Again</button>
                        </div>
                    </div>
                </div>
            </div>
            `)
        })
    })
    // $(".close-modal").click(function(){
    //     $(".modal").classList.add("hidden")
    // })
    // const modal = document.querySelector('.modal');
    // const acc = document.querySelector('.acc-button');
    // const close = document.querySelector('.close-modal');
    // close.addEventListener('click', function() {
    //     modal.classList.add('hidden')
    // });
    // acc.addEventListener('click', function() {
    //     location.href='/campaign'
    // });
// });