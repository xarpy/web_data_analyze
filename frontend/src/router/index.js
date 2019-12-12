import Vue from 'vue';
import VueRouter from 'vue-router';
import PageOne from '../components/PageOne.vue';
import PageTwo from '../components/PageTwo.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'PageOne',
    component: PageOne,
  },
  {
    path: '/logs',
    name: 'PageTwo',
    component: PageTwo,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
