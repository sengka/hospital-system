class Admin::DepartmentsController < ApplicationController
  def index
    @departments = Department.all
  end

  def new
    @department = Department.new
  end

  def create
    @department = Department.new(department_params)

    if @department.save
      redirect_to admin_departments_path, notice: 'Department was successfully created.'
    else
      render :new
    end
  end

  private

  def department_params
    params.require(:department).permit(:name)
  end
end
