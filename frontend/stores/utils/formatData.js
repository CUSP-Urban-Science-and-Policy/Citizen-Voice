import dayjs from "dayjs";
const format = "DD-MM-YYYY";

export const formatDate = (dateString) => { dayjs(dateString).format(format) }
