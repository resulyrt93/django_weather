<template>
  <div class="home-container d-flex justify-content-center py-5 row">
    <div class="col-11 col-sm-10 col-md-9 col-xl-7">
      <div class="row">
        <div class="col-12 col-md-7">
          <div class="container card-wrapper p-3">
            <b-form-select v-model="selectedCity" :options="cities"></b-form-select>
          </div>
        </div>
        <div class="col-12 col-md-5 mt-3 mt-md-0">
          <div class="container card-wrapper p-3 d-flex align-items-center justify-content-center">
            <b-form-group v-slot="{ forecastRadio }">
              <div class="d-flex justify-content-center align-items-center">
                <b-form-radio class="mr-3" v-model="forecastDay" :aria-describedby="forecastRadio" v-bind:value="3">3
                  Days
                </b-form-radio>
                <b-form-radio v-model="forecastDay" :aria-describedby="forecastRadio" v-bind:value="5">5 Days
                </b-form-radio>
              </div>
            </b-form-group>
          </div>
        </div>
      </div>
      <div v-if="selectedCity" class="card-wrapper mt-4 d-flex justify-content-center align-items-center main-card">
        <b-spinner v-if="!dataLoaded" label="Spinning"></b-spinner>
        <div v-if="dataLoaded" class="container p-2">
          <div v-if="dataLoaded" class="container-fluid current-weather">
            <div class="row">
              <div class="col-md-4 col-sm-5">
                <h5>
                  <h3>{{fetchRequest.query}}</h3>
                  <h6>{{timeZone.localtime}}</h6>
                  <h5>{{timeZone.zone}}</h5>
                </h5>
              </div>
              <div class="col-md-5 col-sm-7 d-flex justify-content-center" style="margin: 10px auto;padding:0;">
                <div class="row">
                  <i class="wi"><img v-bind:src="iconUrl"></i>
                  <div class="ml-4">
                    <span class="main-temperature">{{currentCondition.temp_C}}</span>
                    <p class="temp-description">{{currentCondition.weatherDesc[0].value}}</p>
                  </div>
                  <p style="font-size: 1.5rem;">°C</p>
                </div>
              </div>
              <card-right-details :current-condition="currentCondition" :today-detail="todayDetail"/>
            </div>
          </div>
          <div class="container-fluid" style="margin-bottom: 4px">
            <div class="row" style="padding: 2px;">
              <div class="day-weather-box" v-bind:class="forecastDay === 3 ? 'col-md-4' : 'col-md-6'"
                   v-for="nextDay in nextDays" :key="nextDay.date">
                <next-day-box :day-conditions="nextDay"></next-day-box>
              </div>
            </div>
          </div>
          <div class="container-fluid px-0">
            <div style="padding: 2px;">
              <b-button class="detail-expand-button" @click="toggleDetail" v-b-toggle.collapse-1>Show Details</b-button>
              <b-collapse id="collapse-1" class="mt-2">
                <b-card class="detail-card">
                  <div class="detail-card-container">
                    <year-detail-chart v-if="showDetail"
                                       :chart-data="weatherData.ClimateAverages[0].month"></year-detail-chart>
                  </div>
                </b-card>
              </b-collapse>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
    import useWeather from "../hooks/weatherData";
    import NextDayBox from "../components/NextDayBox";
    import CardRightDetails from "../components/CardRightDetails";
    import {appConfig} from "../appConfig";
    import YearDetailChart from "../components/YearDetailChart";

    export default {
        name: 'Home',
        components: {YearDetailChart, CardRightDetails, NextDayBox},
        data: function () {
            return {
                dataLoaded: false,
                forecastDay: 3,
                selectedCity: null,
                weatherData: {},
                showDetail: false
            }
        },
        watch: {
            forecastDay: function () {
                this.showDetail = false
                if (this.selectedCity) {
                  this.getData()
                }
            },
            selectedCity: function () {
                this.showDetail = false
                this.getData()
            }
        },
        computed: {
            currentCondition: function () {
                return this.weatherData.current_condition[0]
            },
            timeZone: function () {
                return this.weatherData.time_zone[0]
            },
            iconUrl: function () {
                return this.weatherData.current_condition[0].weatherIconUrl[0].value
            },
            fetchRequest: function () {
                return this.weatherData.request[0]
            },
            nextDays: function () {
                let days = [...this.weatherData.weather]
                days.shift()
                return days
            },
            todayDetail: function () {
                let days = [...this.weatherData.weather]
                return days.shift()
            },
            cities: function () {
                return appConfig.TURKEY_CITIES
            }
        },
        methods: {
            async getData() {
                this.dataLoaded = false
                this.weatherData = await useWeather(this.forecastDay, this.selectedCity)
                this.dataLoaded = true
            },
            toggleDetail() {
                this.showDetail = !this.showDetail
            }
        }
    }
</script>
<style>
  
  a {
    color: white;
    opacity: 0.6;
    text-decoration: none;
  }
  
  a:hover, a:active, a:focus {
    color: white;
    text-decoration: none;
    opacity: 1;
  }
  
  body {
    background-color: #F4F6F7;
  }
  
  .card-wrapper {
    background-color: #28688C;
    box-shadow: 1px 5px 25px 2px #444;
    border-radius: 10px;
    color: white;
    min-height: 70px;
  }
  
  .card-wrapper .form-group {
    margin-bottom: 0;
  }
  
  .current-weather {
    padding: 15px;
  }
  
  .main-temperature {
    font-size: 5.5em;
    line-height: 0.7;
  }
  
  .main-card {
    min-height: 200px;
  }
  
  .temp-description {
    margin-top: 10px;
    text-align: center;
    display: -webkit-box;
    overflow: hidden;
    text-overflow: ellipsis;
    max-width: 150px;
    -webkit-line-clamp: 1;
    -webkit-box-orient: vertical;
  }
  
  .day-weather-box {
    border: 1px solid #28688C;
    background-color: #2E7FA1;
    border-radius: 5px;
    height: 5em;
  }
  
  .day-weather-box p {
    margin-bottom: 0;
  }
  
  .detail-expand-button {
    width: 100%;
    background-color: #2E7FA1 !important;
    color: #e0e0e0 !important;
    font-weight: 600 !important;
  }
  
  .detail-card {
    background-color: #2E7FA1 !important;
  }
</style>
