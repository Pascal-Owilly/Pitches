function deletePitch(pitchId) {
  fetch("/delete-pitch", {
    method: "POST",
    body: JSON.stringify({ pitchId: pitchId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

const upvote = document.querySelector('#btn_like')
const downvote = document.querySelector('#dislike_btn')


let counter = 0;


upvote.addEventListener('click', like);
downvote.addEventListener('click', dislike);

function like(){
  count++
  counter.innerHTML = count;


}
