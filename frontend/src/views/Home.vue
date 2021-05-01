<template>
  <h1>home</h1>
</template>

<script>
    import useWeather from "../hooks/weatherData";

    export default {
        name: 'Home',
        data: () => {
            return {
                weatherData: {}
            }
        },
        created: async function () {
            const _weatherData = this.getData(4, 'İzmir')
            this.weatherData = _weatherData
        },
        methods: {
            async getData(forecastDay, city) {
                return  await useWeather(forecastDay, city)
            }
        }
    }
</script>
<style>
</style>
