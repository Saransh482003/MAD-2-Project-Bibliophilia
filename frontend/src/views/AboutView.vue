<template>
  <div class="middle">
    <div class="mainPanel">
      <div class="pdfViewer">
        <embed
          src="/Saransh Saini 22F1001123 IIT Madras MAD 2 Project Bibliophilia.pdf"
          width="600"
          height="500"
          type="application/pdf"
          class="pdf"
        />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MyBooksView",
};
</script>

<style scoped>
.middle {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  width: 100%;
  height: 40.1rem;
  background: url("https://github.com/Saransh482003/Image-hosting/blob/main/biblio_bg.jpg?raw=true");
  background-position: center center;
  background-size: cover;
  background-repeat: no-repeat;
}
.mainPanel {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  width: 100%;
  height: 100%;
  padding-bottom: 1.4rem;
  padding-top: 0.7rem;
  overflow: hidden;
  overflow-y: scroll;
}
.pdfViewer {
  width: 90rem;
  height: 200rem;
}
.pdf {
  height: 100%;
  width: 100%;
}
</style>
