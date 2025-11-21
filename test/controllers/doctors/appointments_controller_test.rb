require "test_helper"

class Doctors::AppointmentsControllerTest < ActionDispatch::IntegrationTest
  test "should get index" do
    get doctors_appointments_index_url
    assert_response :success
  end

  test "should get update" do
    get doctors_appointments_update_url
    assert_response :success
  end
end
