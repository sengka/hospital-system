class Admin::DoctorsController < ApplicationController
  def index
    @doctors = User.where(role: :doctor)
  end

  def new
    @doctor = User.new
    @doctor.build_doctor_profile
  end

  def create
    @doctor = User.new(doctor_params)
    @doctor.role = :doctor
    @doctor.password = 'password' # Default password for now

    if @doctor.save
      redirect_to admin_doctors_path, notice: 'Doctor was successfully created.'
    else
      render :new
    end
  end

  private

  def doctor_params
    params.require(:user).permit(:name, :email, doctor_profile_attributes: [:department_id, :room_number, :bio])
  end
end
