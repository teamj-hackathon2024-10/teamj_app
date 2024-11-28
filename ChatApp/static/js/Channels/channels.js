//新規登録ボタン押下時処理

//新規チャンネル追加モーダル
const addChannelModal = document.getElementById("add-channel-modal");
//新規チャンネル追加確認モーダル
const addChannelModalConfirmation = document.getElementById("add-channel-confirmation-modal");

//新規チャンネル追加モーダル表示
document.getElementById("add-channel-button").addEventListener('click',function(event){
    console.log(addChannelModal);
    if(addChannelModal){
    addChannelModal.style.display = "flex"; //モーダルの表示
    }else{
        console.error("モーダルが見つかりません：",addChannelModal);
    }
});

//モーダルを閉じる処理(新規チャンネル追加)
addChannelModal.addEventListener("click", function(e){
    if(e.target === addChannelModal){
        addChannelModal.style.display = "none";
    }
});

//チャンネル追加確認モーダル表示
document.getElementById("add-channel-form").addEventListener("submit",function(event){
    event.preventDefault(); //フォーム送信を行わないようにするため。

    //入力したチャンネル名を取得
    const channelName = document.getElementById('add-channel-input-value').value;
    console.log(channelName);

    //チャンネル名を確認モーダルに表示
    const addChannelDisplay = document.getElementById("add-channel-display");
    console.log(addChannelDisplay);
    addChannelDisplay.value = channelName;
    addChannelDisplay.setAttribute("readonly",true);
    

    //確認モーダルを表示
    if(addChannelModalConfirmation){
        addChannelModalConfirmation.style.display = "flex";
    }else{
        console.error("確認画面のモーダルが見つかりません：",addChannelModalConfirmation);
    }
});

//モーダルを閉じる処理(新規チャンネル追加確認)
addChannelModalConfirmation.addEventListener("click", function(e){
    if(e.target === addChannelModalConfirmation){
        addChannelModalConfirmation.style.display = "none";
    }
});

// 戻るリンクをクリックしたときの処理(チャンネル追加)
document.getElementById('add-back-link').addEventListener('click', function (event) {
    event.preventDefault(); // リンクのデフォルト動作を防ぐ
    // 確認モーダルを閉じる
    document.getElementById("add-channel-confirmation-modal").style.display = "none";
});


//チャンネル編集ボタン押下時処理

//チャンネル編集追加モーダル
const updateChannelModal = document.getElementById("update-channel-modal");
//チャンネル編集確認モーダル
const updateChannelModalConfirmation = document.getElementById("update-channel-confirmation-modal");

//編集ボタンの配列を作成
const editButtons = document.getElementsByClassName("edit-buttons");

//押下したボタンの要素を取得する
for(let i = 0; i < editButtons.length;i++){
    editButtons[i].addEventListener("click",function(){
        const cid = editButtons[i].dataset.cid;
        const channelName = editButtons[i].dataset.channelname;

        console.log("OK");
        console.log("cid :",cid);
        console.log("channelName :",channelName);

        const targetName = document.getElementById("update-channel-input-value");
        targetName.value = channelName;
        targetName.setAttribute("readonly",true);

        if(updateChannelModal){
            updateChannelModal.style.display = "flex";
        }else{
            console.error("モーダルが見つかりません：",updateChannelModal);
        }
    });
}


/*
//チャンネル編集モーダル表示
document.getElementById("update-channel-button").addEventListener('click',function(event){

    console.log(updateChannelModal);
    if(updateChannelModal){
    updateChannelModal.style.display = "flex"; //モーダルの表示
    }else{
        console.error("モーダルが見つかりません：",updateChannelModal);
    }
});
*/

//モーダルを閉じる処理(新規チャンネル追加)
updateChannelModal.addEventListener("click", function(e){
    if(e.target === updateChannelModal){
        updateChannelModal.style.display = "none";
    }
});


//チャンネル編集確認モーダル表示
document.getElementById("update-channel-form").addEventListener("submit",function(event){
    event.preventDefault(); //フォーム送信を行わないようにするため。

    //入力したチャンネル名を取得
    const channelName = document.getElementById('update-channel-input-value').value;
    console.log("編集画面のチャンネル名：",channelName);

    //チャンネル名を確認モーダルに表示
    const updateChannelDisplay = document.getElementById("update-channel-display");
    updateChannelDisplay.value = channelName;
    console.log("入力確定したチャンネル名：",updateChannelDisplay.value);
    updateChannelDisplay.setAttribute("readonly",true);
    

    //確認モーダルを表示
    if(updateChannelModalConfirmation){
        updateChannelModalConfirmation.style.display = "flex";
    }else{
        console.error("確認画面のモーダルが見つかりません：",updateChannelModalConfirmation);
    }
});

//モーダルを閉じる処理(チャンネル編集確認)
updateChannelModalConfirmation.addEventListener("click", function(e){
    if(e.target === updateChannelModalConfirmation){
        updateChannelModalConfirmation.style.display = "none";
    }
});

// 戻るリンクをクリックしたときの処理(チャンネル編集)
document.getElementById('update-back-link').addEventListener('click', function (event) {
    event.preventDefault(); // リンクのデフォルト動作を防ぐ
    // 確認モーダルを閉じる
    document.getElementById("update-channel-confirmation-modal").style.display = "none";
});


//チャンネル削除ボタン押下時処理

//チャンネル削除モーダル
const deleteChannelModal = document.getElementById("delete-channel-modal");
//チャンネル削除確認モーダル
const deleteChannelModalConfirmation = document.getElementById("delete-channel-confirmation-modal");

//ゴミ箱ボタンの配列を作成
const trashButtons = document.getElementsByClassName("trash-buttons");

//押下したボタンの要素を取得する。
for(let i = 0; i < trashButtons.length; i++){
    trashButtons[i].addEventListener("click", function(){
        const cid = trashButtons[i].dataset.cid;
        const channelName = trashButtons[i].dataset.channelname;
        console.log("cid :",cid);
        console.log("channelName :",channelName);

        const targetName = document.getElementById("delete-channel-input-value");
        targetName.innerHTML = channelName;

        console.log(deleteChannelModal);
        if(deleteChannelModal){
        deleteChannelModal.style.display = "flex"; //モーダルの表示
        }else{
            console.error("モーダルが見つかりません：", deleteChannelModal);
        }
        console.log(deleteChannelModalConfirmation);
    });
}

//チャンネル削除確認モーダル表示
document.getElementById("delete-channel-form").addEventListener("submit",function(event){
    event.preventDefault(); //フォーム送信を行わないようにするため。
    //削除対象チャンネル名を取得
    const channelName = document.getElementById('delete-channel-input-value').textContent;
    console.log("削除対象チャンネル名",channelName);

    //チャンネル名を確認モーダルに表示
    const deleteChannelDisplay = document.getElementById("delete-channel-display");
    console.log("チャンネル名",deleteChannelDisplay);
    deleteChannelDisplay.innerHTML = channelName;
    deleteChannelDisplay.setAttribute("readonly",true);
    

    console.log("削除確認モーダル表示：",deleteChannelModalConfirmation);

    //確認モーダルを表示
    if(deleteChannelModalConfirmation){
        deleteChannelModalConfirmation.style.display = "flex";
    }else{
        console.error("確認画面のモーダルが見つかりません：",deleteChannelModalConfirmation);
    }
});

//モーダルを閉じる処理(新規チャンネル追加)
deleteChannelModal.addEventListener("click", function(e){
    if(e.target === deleteChannelModal){
        deleteChannelModal.style.display = "none";
    }
});

//モーダルを閉じる処理(新規チャンネル追加確認)
deleteChannelModalConfirmation.addEventListener("click", function(e){
    if(e.target === deleteChannelModalConfirmation){
        deleteChannelModalConfirmation.style.display = "none";
    }
});

// 戻るリンクをクリックしたときの処理(チャンネル削除)
document.getElementById('delete-back-link').addEventListener('click', function (event) {
    event.preventDefault(); // リンクのデフォルト動作を防ぐ
    // 確認モーダルを閉じる
    document.getElementById("delete-channel-confirmation-modal").style.display = "none";
});