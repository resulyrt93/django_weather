<template>
  <div class="home-container d-flex justify-content-center py-5 row">
    <div class="col-10 col-sm-8 col-md-6">
      <div v-if="dataLoaded" class="container home-wrapper">
        <div class="container-fluid current-weather">
          <div class="row">
            <div class="col-md-4 col-sm-5">
              <h5>
                <span>{{fetchRequest.query}}</span>
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
            
            <!-- Left panel -->
            <div class="col-xs-12 col-sm-12 col-md-3 row" style="text-align: right;">
              <div class="col-md-12 col-sm-3 col-xs-3 side-weather-info">
                <h6>Humidity:
                  <span>{{currentCondition.humidity}}</span>
                  %
                </h6>
              </div>
              <div class="col-md-12 col-sm-3 col-xs-3 side-weather-info">
                <h6>Wind:
                  <span>{{currentCondition.windspeedKmph}}</span>
                  KMPH
                </h6>
              </div>
              <div class="col-md-12 col-sm-3 col-xs-3 side-weather-info">
                <h6>High:
                  <span>{{todayDetail.maxtempC}}</span>
                  °
                </h6>
              </div>
              <div class="col-md-12 col-sm-3 col-xs-3 side-weather-info">
                <h6>Low:
                  <span>{{todayDetail.mintempC}}</span>
                  °
                </h6>
              </div>
            </div>
          
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
</template>

<script>
    import useWeather from "../hooks/weatherData";
    import NextDayBox from "../components/NextDayBox";

    export default {
        name: 'Home',
        components: {NextDayBox},
        data: () => {
            return {
                dataLoaded: false,
                forecastDay: 3,
                weatherData: {}
            }
        },
        computed: {
            currentCondition: function () {
                return this.weatherData.current_condition[0]
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
            }
        },
        created: async function () {
            const _weatherData = await this.getData(4, 'İzmir')
            this.weatherData = _weatherData
            this.dataLoaded = true
        },
        methods: {
            async getData(forecastDay, city) {
                return await useWeather(forecastDay, city)
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
  
  .active {
    color: white;
    text-decoration: none;
    opacity: 1;
  }
  
  body {
    background-color: #F4F6F7;
  }
  
  .home-wrapper {
    background-color: #28688C;
    box-shadow: 1px 5px 25px 3px #444;
    border-radius: 10px;
    margin: 100px auto;
    max-width: 720px;
    padding: 0px;
    color: white;
  }
  
  .current-weather {
    padding: 15px;
  }
  
  .main-temperature {
    font-size: 5.5em;
    line-height: 0.7;
  }
  
  .temp-description {
    margin-top: 10px;
    text-align: center;
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
  
  .side-weather-info {
    padding: 0px 10px;
  }
</style>
