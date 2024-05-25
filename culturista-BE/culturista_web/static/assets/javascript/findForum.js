function findForum(){
    fetch("http://127.0.0.1:8000/api/find-forum/title=" + $('#title').val())
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        console.log(data);
        
        // delete old column
        const elements = document.getElementsByClassName('topic-conlumns');
        while(elements.length > 0){
            elements[0].parentNode.removeChild(elements[0]);
        }

        // add column
        var topicList = document.getElementsByClassName('topic-list')[0];

        for (var i = 0; i<data.content_id.length; i++){            
            // create column
            var column = document.createElement("div");
            column.className = "topic-conlumns";

            // create topic content
            var topic_content = document.createElement("div");
            topic_content.className = "topic-content";

            // create a link
            var topic_link = document.createElement("a");
            topic_link.href = "http://127.0.0.1:8000/api/forum/" + data.content_id[i];

            // create topic name
            var topic_name = document.createElement("h4");
            topic_name.className = "topic-name";
            topic_name.innerHTML = data.titles[i];

            // create replies
            var replies = document.createElement("h4");
            replies.className = "replies-nums";
            replies.innerHTML = data.replies[i];

            // create tag
            var topic_tag = document.createElement("div");
            topic_tag.className = "topic-tags";

            // create repies
            var tag_content = document.createElement("p");
            tag_content.innerHTML = data.tag[i];

            topic_link.appendChild(topic_name);
            topic_content.appendChild(topic_link);
            topic_content.append(replies);

            topic_tag.appendChild(tag_content);

            column.appendChild(topic_content);
            column.appendChild(topic_tag);
            
            topicList.appendChild(column);
        }
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });
}