<template>
  <div class="errorPage">
    <p class="oops">Oops!</p>
    <p class="titleMessage">500 - Unable to Fetch Data</p>
    <p class="message">
      Sorry! We were unable to fetch your books. Try checking your internet
      connection.
    </p>
  </div>
</template>

<script>
export default {
  name: "ErrorPage",
  props: {
    msg: {
      type: String,
      required: true,
      default: "404 - PAGE NOT FOUND",
    },
  },
};
</script>

<style scoped>
.errorPage {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  align-items: center;
  width: 100%;
  height: 34.6rem;
}
.oops {
  font-size: 15rem;
  font-weight: 900;
  background: url("@/assets/images/booksErrorBg.png");
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
}
.titleMessage {
  font-size: 2rem;
  text-transform: uppercase;
  letter-spacing: 2px;
  font-weight: 800;
}
.message {
  width: 30%;
  text-align: center;
  margin-top: 0.5rem;
  margin-bottom: 2rem;
}
</style>
