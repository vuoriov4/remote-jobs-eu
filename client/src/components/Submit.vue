<template>
  <div id="submit">
    <h2 id="submit-title">Submit a job</h2>
    <input placeholder="Title" v-model="job.job_title"/>
    <input placeholder="Description" v-model="job.job_description"/>
    <input placeholder="Salary range min" v-model="job.salary_range_min"/>
    <input placeholder="Salary range max" v-model="job.salary_range_max"/>
    <input placeholder="Latitude" v-model="job.latitude"/>
    <input placeholder="Longitude" v-model="job.longitude"/>
    <input placeholder="City" v-model="job.city"/>
    <input placeholder="Country" v-model="job.country"/>
    <input placeholder="Municipality" v-model="job.municipality"/>
    <button @click="submit">Submit</button>
  </div>
</template>

<script>
  import api from '../api';
  export default {
    name: 'Submit',
    components: {},
    data() {
      return {
        job: {
          'job_title': 'Developer wanted',
          'job_description': 'Job description',
          'salary_range_min': 10000,
          'salary_range_max': 80000,
          'latitude': 64.37,
          'longitude': 22.28,
          'city': 'Oulu',
          'country': 'Finland',
          'municipality': 'Pohjois-pohjanmaa',
        }
      };
    },
    methods: {
      submit() {
        console.log("submit");
        const res = api.upload(this.job);
        console.log(res);
      }
    }
  };
</script>

<style>
  #submit {
    height: 100%;
    background: #f0f0f0;
  }
  #submit-title {
    margin: 0px;
    color: black;
    padding: 25px 0px 10px 30px;
  }
</style>