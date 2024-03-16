<template>
  <div id="app">
    <router-view></router-view>
    <FlashMessage :position="'right bottom'"></FlashMessage>

  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  // components: {
  //   // HelloWorld
  // }
}
</script>

<style>

</style>
