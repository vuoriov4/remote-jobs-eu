<template>
  <div id="map">
    <MglMap 
      @click="onMapClick" 
      :accessToken="accessToken" 
      :mapStyle.sync="mapStyle"
      @load="onMapLoaded" 
      :zoom="zoom" 
      :center="center">
      <template v-for="(job, i) in jobs">
        <MglMarker v-if="job.lon && job.lat"
        :coordinates="[job.lon, job.lat].map(x => x + 0.5 * (Math.random() - Math.random()))" 
        :color="job._color" 
        :showed="job._showed" 
        v-bind:key="'marker-' + i">
          <MglPopup @open="onPopupOpen">
            <job-card 
              @select-job-description="data => $emit('select-job-description', data)"
              @select-company="data => $emit('select-company', data)" 
              @select-location="data => $emit('select-location', data)"
              :job="job">
            </job-card>
          </MglPopup>
        </MglMarker>
      </template>
    </MglMap>
  </div>
</template>
<script>
import Mapbox from "mapbox-gl";
import '../../node_modules/mapbox-gl/dist/mapbox-gl.css'; 
import { MglMap, MglMarker, MglPopup } from "vue-mapbox";
import JobCard from './JobCard.vue';

export default {
  name: 'MapView',
  components: {
    MglMap, MglMarker, MglPopup, JobCard
  },
  props: ['jobs', 'center', 'zoom'],
  data() {
    return {
      accessToken: 'pk.eyJ1IjoidnVvcmlvdjQiLCJhIjoiY2pnY240YnFvMmFxODJxczAzbnBxYTR0OSJ9.xd_N9Vuak-g3bn8Y5sbXRQ',
      mapStyle: 'mapbox://styles/mapbox/light-v10', // your map style
    };
  },
  watch: {
    center() {
      if (!this.map) return;
      this.map.flyTo({ center: this.center });
    }
  },
  methods: {
    onMapLoaded(event) {
      this.map = event.map;
    },
    onMapClick(event) {
      console.log(event.mapboxEvent.lngLat);
    },
    onPopupOpen() {
      /*
      const job_title = obj.popup._content.getElementsByClassName('mgl-popup-title')[0].innerHTML;
      const job = this.jobs.find(x => x.title === job_title);
      if (job) {
        this.$emit('select-marker', job);
      }
      */
    }
  },
  created() {
    this.map = null;
  },
  async mounted() {
    this.mapbox = Mapbox;
  }
};
</script>
<style>
  #map, .mapboxgl-canvas-container {
    width: calc(100%);
    height: calc(100vh - 80px);
    position: fixed;
    top: 80px;
    z-index: 1;
    pointer-events: all;
  }
  .mapboxgl-popup {
    z-index: 9999999;
  }
  .mapboxgl-popup-content {
    margin: 0px !important;
    padding: 0px !important;
  }
  .mapboxgl-popup-content > .job {
    border: 1px solid black;
    width: 400px;
    padding: 20px;
    margin: 0px;
  }
  .mapboxgl-popup-close-button {
    transform: scale(2.0) translate(-2px, 2px) !important;
  }
</style>