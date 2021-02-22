const file_picker = document.querySelector("#id_file")
const image_container = document.querySelector("#image_container")

const addFileName = (e) => {
    const elem = document.querySelector("#filename");
    elem.classList.add('form__label');
    elem.style = 'float:right; margin-top:15px';
    elem.innerHTML = `<span> ${file_picker.files[0].name}</span> <span class="form__field-item-delete"></span>`;
    image_container.addEventListener('click', deleteFileName);
};

const deleteFileName = (e) => {
    if(e.target.classList.contains('form__field-item-delete')) {
            image_container.removeEventListener('click', deleteFileName);
            const elem = document.querySelector("#filename");
            elem.style = 'display:none'
            file_picker.value = "";
        };
};

file_picker.addEventListener('change', addFileName);
