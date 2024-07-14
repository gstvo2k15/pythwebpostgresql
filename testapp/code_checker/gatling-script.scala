import io.gatling.core.Predef._
import io.gatling.http.Predef._
import scala.concurrent.duration._

class BasicSimulation extends Simulation {

  val httpProtocol = http
    .baseUrl("http://nginx") // URL base de tu API
    .acceptHeader("application/json")

  val scn = scenario("Basic Load Test")
    .exec(http("request_1")
    .get("/api/"))
    .pause(5) // Pausa de 5 segundos entre solicitudes

  setUp(
    scn.inject(
      atOnceUsers(10), // 10 usuarios simultáneos
      rampUsers(100) during (10 seconds) // 100 usuarios durante 10 segundos
    ).protocols(httpProtocol)
  )
}

