mod plane_figures;

use cucumber::World;
use plane_figures::PlaneTest;

#[tokio::main]
async fn main() {
    PlaneTest::run("features/plane_figures.feature").await;
}
