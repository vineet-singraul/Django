function showSearchBox() {
    var searchBoxDiv = document.getElementById("searchBoxDiv");
    var existingInput = document.getElementById("myInput");

    if (existingInput == null) {
        searchBoxDiv.innerHTML = `
        <div class="searchBoxDiv">
            <input type="text" id="myInput" placeholder="Type to search...">
            <button>Search</button>
        </div>
        `;
    }
    else{
        searchBoxDiv.innerHTML = " "
    }
}