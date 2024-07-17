import fastify from "fastify";
import cors from "@fastify/cors"
import { validatorCompiler, serializerCompiler } from "fastify-type-provider-zod";
import { createTrip } from "./routes/create-trip";
import { confirmTrip } from "./routes/confirm-trip";
import { confirmParticipant } from "./routes/confirm-participant";
import { createActivity } from "./routes/create-activity";
import { getActivities } from "./routes/get-activities";
import { createLink } from "./routes/create-link";
import { getLinks } from "./routes/get-links";
import { createInvite } from "./routes/create-invite";
import { getParticipants } from "./routes/get-participants";
import { getParticipant } from "./routes/get-participant";
import { updateTrip } from "./routes/update-trip";
import { getTripDetails } from "./routes/get-trip-details";
import { errorHandler } from "./error-handler";
import { env } from "./env";

const app = fastify()

app.register(cors, {
    origin: env.WEB_BASE_URL
})


app.setValidatorCompiler(validatorCompiler);
app.setSerializerCompiler(serializerCompiler);

app.setErrorHandler(errorHandler)

app.register(createTrip)
app.register(confirmTrip)
app.register(confirmParticipant)
app.register(createActivity)
app.register(getActivities)
app.register(createLink)
app.register(getLinks)
app.register(createInvite)
app.register(getParticipants)
app.register(getParticipant)
app.register(updateTrip)
app.register(getTripDetails)

app.listen({ port: env.PORT }).then(() => {
    console.log("Server running!")
})