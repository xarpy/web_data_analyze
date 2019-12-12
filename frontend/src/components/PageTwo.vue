<template>
  <div class="container">
      <div class="row">
      <div class="col-sm-10">
        <h1 class="display-4">Logs</h1>
        <hr class="my-4">
        <div class="jumbotron">
        <p>{{list}}</p>
        </div>
        <br><br>
      </div>
    </div>
    </div>
</template>
<script>
import axios from 'axios';

export default {
  name: 'PageTwo',
  data() {
    return {
      list: '',
    };
  },
  methods: {
    getLogs() {
      axios.get('http://localhost:5000/data/logs', {
        headers: {
          'Content-Type': 'application/json',
        },
      }).then((res) => {
        this.msg = res.data;
      }).catch((error) => {
        console.log(error);
      });
    },
  },
  created() {
    this.getLogs();
  },
};
</script>
