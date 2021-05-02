<template>
  <div class="home-container d-flex justify-content-center py-5 row">
    <div class="col-10 col-sm-8 col-md-6">
      <div class="container card-wrapper p-3">
        <b-form-select v-model="selectedCity" :options="cities" @change="getData"></b-form-select>
      </div>
      <div class="card-wrapper mt-4 d-flex justify-content-center align-items-center main-card">
        <b-spinner v-if="!dataLoaded" label="Spinning"></b-spinner>
        <div v-if="dataLoaded && selectedCity" class="container p-2">
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
          <div class="container-fluid">
            <div class="row" style="padding: 2px;">
              <div class="col-md-4 day-weather-box" v-for="nextDay in nextDays" :key="nextDay.date">
                <next-day-box :day-conditions="nextDay"></next-day-box>
              </div>
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

    export default {
        name: 'Home',
        components: {CardRightDetails, NextDayBox},
        data: () => {
            return {
                dataLoaded: false,
                forecastDay: 4,
                selectedCity: '',
                weatherData: {}
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
        created: async function () {
            // const _weatherData = await this.getData(4, this.selectedCity)
            // this.weatherData = _weatherData
            this.dataLoaded = true
        },
        methods: {
            async getData(city) {
                this.dataLoaded = false
                this.weatherData = await useWeather(this.forecastDay, city)
                this.dataLoaded = true
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
    box-shadow: 1px 5px 25px 3px #444;
    border-radius: 10px;
    color: white;
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
    overflow : hidden;
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
</style>
