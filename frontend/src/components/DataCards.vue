<template>
  <div class="dataCard">
    <p class="dataCardHead">
      {{ cardHead }}
    </p>
    <p class="dataCardValue">
      {{ cardValue }}
    </p>
  </div>
</template>

<script>
export default {
  name: "DataCard",
  props: {
    cardHead: {
      type: String,
      required: true,
    },
    cardValue: {
      type: String,
      required: true,
    },
  },
};
</script>

<style scoped>
.dataCard {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 15.9rem;
  height: 80%;
  margin: 1rem;
  border-radius: 1rem;
  box-shadow: 0 0.25rem 1rem #00000026;
  backdrop-filter: blur(30px);
  -webkit-backdrop-filter: blur(30px);
  border: 1px solid rgba(255, 255, 255, 0.3);
}
.dataCardHead {
  font-size: 0.7rem;
  font-weight: 600;
  color: rgb(71, 71, 71);
}
.dataCardValue {
  font-size: 4rem;
  font-weight: 800;
  /* color: rgb(71, 71, 71); */
  background: linear-gradient(
    200deg,
    rgba(121, 241, 164, 1),
    rgba(71, 171, 168, 1),
    rgba(71, 171, 168, 1),
    rgba(71, 171, 168, 1)
  );
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  /* -webkit-text-stroke: 1px white; */
}
</style>
