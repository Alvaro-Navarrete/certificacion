document.addEventListener('DOMContentLoaded', function () {


    // Toast

    // var toastBoostrap
    const toastElement = document.getElementById('toast')
    if (toastElement) {
        const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastElement)
        toastBootstrap.show()
    }

    // Modal

    document.getElementById('btn-modal').addEventListener('click',function(){
        const modal = new bootstrap.Modal(document.getElementById('modal-mensaje'))
        modal.show()
    })


    document.getElementById('botonSubmit').addEventListener('click', function(){
        
        const formulario = document.getElementById('miFormulario')

        formulario.submit()
    })

})
