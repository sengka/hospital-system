require "test_helper"

class Admin::DepartmentsControllerTest < ActionDispatch::IntegrationTest
  test "should get index" do
    get admin_departments_index_url
    assert_response :success
  end

  test "should get new" do
    get admin_departments_new_url
    assert_response :success
  end

  test "should get create" do
    get admin_departments_create_url
    assert_response :success
  end
end
