<template>
  <div id="app">
    <div id="top">
      <div id="top-title">Find remote {{ dev }} jobs in Europe</div>
      <input autofocus id="search-bar" placeholder="🔎 React, AWS, C++, Azure" v-model="searchTerm"/>
      <img src="loading.gif" id="loading-gif" v-if="loading"/>
      <a href="https://github.com/vuoriov4/remote-jobs-eu"><img src="github.png" id="github" width="30px"/></a>
    </div>
    <div id="app-content" v-if="response">
      <div id="left">
        <job-list 
          @select-job-description="selectJobDescription"
          @select-company="selectCompany" 
          @select-location="selectLocation" 
          @select-order-by="selectOrderBy"
          @select-num-results="selectNumResults"
          @select-created-since="selectCreatedSince"
          :response="response"/>
      </div>
      <div class="right-content" id="content-job-description" v-if="showJobDescription">
        <job-description :job="job" @close="close()"/>
      </div>
      <div class="right-content" id="content-ratings" v-if="showCompany">
        <company :job="job" @close="close()"/>
      </div>
      <map-view 
        :jobs="response.jobs" 
        :center="mapCenter" 
        :zoom="zoom"
        @select-job-description="selectJobDescription"
        @select-company="selectCompany" 
        @select-location="selectLocation">
      </map-view>
    </div>
    <div id="footer"></div>
  </div>
</template>

<script>
import api from './api';
import JobList from './components/JobList.vue';
import JobDescription from './components/JobDescription.vue';
import Company from './components/Company.vue';
import MapView from './components/MapView.vue';

export default {
  name: 'App',
  components: {
    JobList, JobDescription, Company, MapView,
  },
  data() {
    return {
      response: null,
      job: null,
      loading: true,
      devs: ['👨🏻‍💻', '👨‍💻', '👨🏽‍💻', '👩🏻‍💻', '👨🏻‍💻', '👨🏻‍💻', '👨🏻‍💻', '👨🏻‍💻', '👨🏼‍💻', '👩‍💻', ],
      dev: '👨🏻‍💻',
      showJobDescription: false,
      showCompany: false,
      mapCenter: [-10, 51],
      zoom: 3.1,
      searchTerm: '',
      orderBy: 'relevance',
      numResults: 50,
      createdSince: parseInt((Date.now() / 1000) - 60 * 60 * 24 * 7),
      abortController: new AbortController(),
    };
  },
  methods: {
    async getJobData(searchTerm, orderBy, numResults, createdSince, signal) {
      this.loading = true;
      const data = await api.query(
        searchTerm, 
        orderBy, 
        numResults, 
        createdSince,
        signal);
      data.jobs.forEach(job => {
        job['_showed'] = true;
        job['_color'] = '#20C20E';
      });
      this.response = data;
      this.loading = false;
      console.log(data);
    },
    selectJobDescription(e) {
      this.showJobDescription = true;
      this.showCompany = false;
      this.job = e;
    },
    selectCompany(e) {
      this.showJobDescription = false;
      this.showCompany = true;
      this.job = e;
    },
    selectLocation(e) {
      this.showJobDescription = false;
      this.showCompany = false;
      this.job = e;
      this.mapCenter = [22.2666, 60.4518];
      this.zoom = 4.0;
    },
    selectOrderBy(e) {
      this.orderBy = e.target.value;
      this.getJobData(this.searchTerm, this.orderBy, this.numResults, this.createdSince);
    },
    selectNumResults(e) {
      this.numResults = e.target.value;
      this.getJobData(this.searchTerm, this.orderBy, this.numResults, this.createdSince);
    },
    selectCreatedSince(e) {
      this.createdSince = e.target.value;
      this.getJobData(this.searchTerm, this.orderBy, this.numResults, this.createdSince);
    },
    close() {
      this.showCompany = false;
      this.showJobDescription = false;
    },
    onInputChange(e) {
      console.log(e);
    },
  },
  watch: {
    async searchTerm() {
      if (this.searchTerm.length > 0 && this.searchTerm.length < 3) return;
      if (this.loading) this.abortController.abort();
      this.abortController = new AbortController();
      await this.getJobData(
        this.searchTerm, 
        this.orderBy, 
        this.numResults, 
        this.createdSince,
        this.abortController.signal);
    },
  },
  async mounted() {
    await this.getJobData(this.searchTerm, this.orderBy, this.numResults, this.createdSince);
    setInterval(() => {
      this.dev = this.devs[(this.devs.indexOf(this.dev) + 1) % this.devs.length];
    }, 1000);
  }
};
</script>
<style>
  body, #app {
    width: 100%;
    height: 100%;
    padding: 0px;
    margin: 0px;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 18px;
    color: #202040;
  } 
  a {
    color: #20C20E;
  }
  #top {
    height: 80px;
    width: 100%;
    background: #202020;
    color: white;
    text-align: center;
    font-weight: bold;
    line-height: 80px;
    font-size: 26px;
  }
  .top-link {
    margin-right: 20px;
    float: right;
  }
  #top-title {
    margin-left: 20px;
    float: left;
  }
  #github {
    float: right;
    transform: translate(-25px, 25px);
  }
  #search-bar {
    float: left;
    height: 20px;
    margin: 20px 0px 0px 20px;
    width: 460px;
    border-radius: 5px;
    border: none;
    padding: 10px;
    font-size: 18px;
    color: #808080;
  }
  .right-content {
    width: 612px;
    height: calc(100vh - 140px);
    position: fixed;
    top: 40px;
    left: 612px;
    margin: 40px;
    z-index: 1;
    pointer-events: all;
    background: white;
    padding: 30px 40px 30px 40px;
    z-index: 99;
    overflow-y: auto;
    box-shadow: 5px 0px 10px rgba(0,0,0,0.2);
    background: white;
  }
  #left {
    overflow-y: auto;
    width: 640px;
    height: calc(100vh - 100px);
    background: #f0f0f0;
    z-index: 2;
    padding: 10px 10px;
    position: fixed;
    box-shadow: 5px 0px 10px rgba(0,0,0,0.2);
  }
  #app-content {
  }
  #loading-gif {
    height: 30px;
    float: left;
    margin: 25px 0px 0px 15px;
    opacity: 0.5;
  }
  #footer {
    width: 100%;
    height: 0px;
    background: rgba(255,255,255,0.5);
    position: fixed;
    bottom: 0px;
    z-index: 2;
  }
  .close-btn {
    position: absolute;
    top: 0px;
    border: none;
    font-size: 22px;
    top: 32.5px;
    right: 32.5px;
    cursor: pointer;
  }
  hr {
    margin-top: -10px;
  }
</style>