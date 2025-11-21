require "test_helper"

class Admin::DoctorsControllerTest < ActionDispatch::IntegrationTest
  test "should get index" do
    get admin_doctors_index_url
    assert_response :success
  end

  test "should get new" do
    get admin_doctors_new_url
    assert_response :success
  end

  test "should get create" do
    get admin_doctors_create_url
    assert_response :success
  end
end
