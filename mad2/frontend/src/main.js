import {BootstrapVue, BootstrapVueIcons, FormFilePlugin,ImagePlugin } from 'bootstrap-vue' 
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import FlashMessage from '@smartweb/vue-flash-message'


import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
// import { from } from 'core-js/core/array';

Vue.config.productionTip = false


Vue.use(BootstrapVue);
Vue.use(BootstrapVueIcons);
Vue.use(FormFilePlugin);
Vue.use(ImagePlugin);

Vue.use(FlashMessage,
  {
    name: 'flashMessage',
    tag: "FlashMessage",
    time: 4000,
    strategy: "multiple"
  })

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
