import axios from "axios";
import {appConfig} from "./appConfig";

const configureRequest = () => {
    const request = axios.create({
        baseURL: appConfig.API_URL,
        timeout: 120000
    })
    return request
}

export const request = configureRequest()
