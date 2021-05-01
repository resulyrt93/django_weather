import {request} from "../request";
import {appConfig} from "../appConfig";


export default async function useWeather (forecastDay=3, city) {
    try {
        const res = await request.post(appConfig.WEATHER_DATA_PATH, {city, forecast_day: forecastDay})
        const {data} = res
        return data
    } catch (e) {
        console.log("Error : ", e)
    }
}
