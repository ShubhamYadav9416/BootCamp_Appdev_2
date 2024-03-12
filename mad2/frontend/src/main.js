import {BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue' 

import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
// import { from } from 'core-js/core/array';

Vue.config.productionTip = false


Vue.use(BootstrapVue);
Vue.use(BootstrapVueIcons);

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
