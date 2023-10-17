function toggleModal(url) {
    window.open(url)
}

const uploadModal = document.querySelector(".upload-modal");
const fileInput = uploadModal.querySelector("input");


function openModal() {
    uploadModal.classList.add('is-active')
}

function uploadFile() {
    const file = fileInput.files[0];
    console.log(file)
    // Здесь выполняем логику загрузки файла
       uploadModal.classList.remove('is-active')

}