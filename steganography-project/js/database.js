let db;

let request = indexedDB.open("StegoDB",1);

request.onupgradeneeded = function(){
    db = request.result;

    if(!db.objectStoreNames.contains("users")){
        db.createObjectStore("users",{keyPath:"username"});
    }
};

request.onsuccess = function(){
    db = request.result;
};